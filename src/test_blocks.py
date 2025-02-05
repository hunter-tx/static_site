import unittest
from markdown_blocks import *

class TestBlocks(unittest.TestCase):
    # def test_split_block(self):
    #     markdown = ("# This is a heading\n"
    #                 "\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n"
    #                 "\n* This is the first list item in a list block\n* This is a list item"
    #                 "\n* This is another list item")
    #     test = markdown_to_blocks(markdown)
    #     expected = ["# This is a heading",
    #                 "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
    #                 "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
    #                 ]
    #     self.assertEqual(test, expected)
    #
    # def test_extra_lines(self):
    #     markdown = ("# This is the heading\n\n"
    #                 "This is the first line of text\n\n\n\n\n"
    #                 "There are too many new lines here\n\n"
    #                 "This one is good\n\n\n"
    #                 "This one is not")
    #     test = markdown_to_blocks(markdown)
    #     expected = ["# This is the heading", "This is the first line of text", "There are too many new lines here",
    #                 "This one is good", "This one is not"]
    #     self.assertEqual(test, expected)
    #
    # def test_strip_whitespace(self):
    #     markdown = ("     # This is the heading     \n\n"
    #                 "  This is the first line of text \n\n\n\n\n"
    #                 " There are too many new lines here    \n\n"
    #                 "   This one is good  \n\n\n"
    #                 "       This one is not")
    #     test = markdown_to_blocks(markdown)
    #     expected = ["# This is the heading", "This is the first line of text", "There are too many new lines here",
    #                 "This one is good", "This one is not"]
    #     self.assertEqual(test, expected)

    def test_block_types_heading(self):
        block = "## This is a heading"
        test = block_to_block_type(block)
        expected = "heading"
        self.assertEqual(test, expected)

    def test_block_types_code(self):
        block = "```this is\nthree lines\nof code\n```"
        test = block_to_block_type(block)
        expected = "code"
        self.assertEqual(test, expected)

    def test_block_types_paragraph(self):
        block = "This block it just\none big long paragraph\nnothing special here."
        test = block_to_block_type(block)
        expected = "paragraph"
        self.assertEqual(test, expected)

    def test_block_types_quote(self):
        block = ">This is a quote\n>a very long quote"
        test = block_to_block_type(block)
        expected = "quote"
        self.assertEqual(test, expected)

    def test_block_types_unordered_list(self):
        block = "* This is a list\n* a very short list\n* one with only a few items\n* maybe one more"
        test = block_to_block_type(block)
        expected = "unordered_list"
        self.assertEqual(test, expected)

    def test_block_types_ordered_list(self):
        block = "1. This is a list\n2. a very short list\n3. one with only a few items\n4. maybe one more"
        test = block_to_block_type(block)
        expected = "ordered_list"
        self.assertEqual(test, expected)


if __name__ == "__main__":
    unittest.main()