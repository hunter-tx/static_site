from htmlnode import *
from textnode import *



def markdown_to_blocks(markdown):
    split_strings = markdown.split("\n\n")
    returned_list = []
    for string in split_strings:
        if not string:
            continue
        returned_list.append(string.strip())
    return returned_list

def block_to_block_type(block):
    lines = block.split("\n")
    if lines[0].startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return "heading"
    if lines[0].startswith("```") and lines[-1].startswith("```"):
        return "code"
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return "paragraph"
        return "quote"
    if block.startswith("* "):
        for line in lines:
            if not line.startswith("* "):
                return "paragraph"
        return "unordered_list"
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return "paragraph"
        return "unordered_list"
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return "paragraph"
            i += 1
        return "ordered_list"

    return "paragraph"


def markdown_to_html_node(markdown):
    child_nodes = []
    blocks = markdown.split("\n\n")
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == "paragraph":
            child_nodes.append(paragraph_to_html_node(block))
        if block_type == "heading":
            child_nodes.append(heading_to_html_node(block))
        if block_type == "code":
            child_nodes.append(code_to_html_node(block))
        if block_type == "quote":
            child_nodes.append(quote_to_html_node(block))
        if "list" in block_type:
            child_nodes.append(list_to_html_node(block))

    return ParentNode(tag="div", children=child_nodes)

def paragraph_to_html_node(block):
    return LeafNode("p", block)

def heading_to_html_node(block):
    header_num = block.count("#")
    text = block.strip("#").strip()
    return LeafNode(tag=f"h{header_num}", value=text)

def code_to_html_node(block):
    text = block.strip("```").strip("\n")
    return LeafNode("code" ,text)

def quote_to_html_node(block):
    quote_lines = block.split("\n")
    for i in range(len(quote_lines)):
        quote_lines[i] = quote_lines[i][1:]
    text = "\n".join(quote_lines)
    return LeafNode("blockquote", text)

def list_to_html_node(block):
    type = block_to_block_type(block)
    if type == "unordered_list":
        tag = "ul"
    elif type == "ordered_list":
        tag = "ol"
    list_items = block.split("\n")
    for i in range(len(list_items)):
        if type == "unordered_list":
            list_items[i] = list_items[i][2:]
        elif type == "ordered_list":
            list_items[i] = list_items[i][3:]
    list_children = []
    for item in list_items:
        list_children.append(LeafNode(tag="li", value=item))
    return ParentNode(tag, list_children)
