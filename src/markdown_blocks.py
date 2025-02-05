def markdown_to_blocks(markdown):
    split_strings = markdown.split("\n\n")
    returned_list = []
    for string in split_strings:
        if not string:
            continue
        returned_list.append(string.strip())
    return returned_list