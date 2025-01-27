from textnode import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            text_list = node.text.split(delimiter)
            if len(text_list) % 2 == 0:
                raise Exception("delimiter not closed in markdown. improper syntax")
            for i in range(len(text_list)):
                if (i + 1) % 2 != 0: # even values will be of TextType.TEXT, odd will be within the delimiters
                    new_nodes.append(TextNode(text_list[i], TextType.TEXT))
                else:
                    new_nodes.append(TextNode(text_list[i], text_type))
    return new_nodes
