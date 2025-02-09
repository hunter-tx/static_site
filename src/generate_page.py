import os
import shutil

from htmlnode import *
from textnode import *
from inline_markdown import *
from markdown_blocks import *

markdown_path = "./content/index.md"
template_path = "./template.html"
destination_path = "./public/index.html"
content_path = "./content"

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from{from_path} to {dest_path} using {template_path}...")
    markdown = open(from_path, "r")
    markdown_text = markdown.read()
    markdown.close()
    template = open(template_path, "r")
    template_text = template.read()
    template.close()
    markdown_as_html = markdown_to_html_node(markdown_text).to_html()
    title = extract_title(markdown_text)
    template_text = template_text.replace("{{ Title }}", title)
    template_text = template_text.replace("{{ Content }}", markdown_as_html)
    with open(destination_path, "w") as file:
        file.write(template_text)
    print("Page generated")

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    if os.path.exists(dir_path_content):
        contents = os.listdir(dir_path_content)  # returns list of files/directories in current directory
        for content in contents:
            if content.startswith("."):
                continue
            source_filepath = dir_path_content + f"/{content}"
            destination_filepath = dest_dir_path + f"/{content}"
            if os.path.isfile(source_filepath):
                generate_page(source_filepath, template_path, destination_filepath)
            else:
                os.mkdir(destination_filepath)
                generate_pages_recursive(source_filepath,template_path, destination_filepath)

