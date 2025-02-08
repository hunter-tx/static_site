from htmlnode import *
from textnode import *
from inline_markdown import *
from markdown_blocks import *

markdown_path = "/Users/hunterhughes/Coding/workspace/github.com/hunter-tx/static_site/content/index.md"
template_path = "/Users/hunterhughes/Coding/workspace/github.com/hunter-tx/static_site/template.html"
destination_path = "/Users/hunterhughes/Coding/workspace/github.com/hunter-tx/static_site/public/index.html"

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


generate_page(markdown_path, template_path, destination_path)