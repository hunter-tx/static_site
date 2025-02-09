import os
import shutil
from textnode import *
from htmlnode import *
from markdown_blocks import *
from generate_page import *

SOURCE = "./static"
DESTINATION = "./public"
content_path = "./content"
template_path = "./template.html"
destination_path = "./public"

def main():
    print("Deleting public directory...")
    if os.path.exists(DESTINATION):
        shutil.rmtree(DESTINATION)
    os.mkdir(DESTINATION)
    print("Copying static files to public directory...")
    copy_source_to_destination(SOURCE,DESTINATION)
    generate_pages_recursive(content_path, template_path, destination_path)

def copy_source_to_destination(source, destination):
    if os.path.exists(source):
        contents = os.listdir(source) # returns list of files/directories in current directory
        for content in contents:
            source_filepath = source + f"/{content}"
            destination_filepath = destination + f"/{content}"
            if os.path.isfile(source_filepath):
                shutil.copy(source_filepath, destination_filepath)
            else:
                os.mkdir(destination_filepath)
                copy_source_to_destination(source_filepath, destination_filepath)

main()

