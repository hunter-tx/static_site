import unittest
from markdown_blocks import *

class TestBlocks(unittest.TestCase):
    def test_split_block(self):
        markdown = ("# This is a heading\n"
                    "\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n"
                    "\n* This is the first list item in a list block\n* This is a list item"
                    "\n* This is another list item")
        test = markdown_to_blocks(markdown)
        expected = ["# This is a heading",
                    "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
                    "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
                    ]
        self.assertEqual(test, expected)

    def test_extra_lines(self):
        markdown = ("# This is the heading\n\n"
                    "This is the first line of text\n\n\n\n\n"
                    "There are too many new lines here\n\n"
                    "This one is good\n\n\n"
                    "This one is not")
        test = markdown_to_blocks(markdown)
        expected = ["# This is the heading", "This is the first line of text", "There are too many new lines here",
                    "This one is good", "This one is not"]
        self.assertEqual(test, expected)

    def test_strip_whitespace(self):
        markdown = ("     # This is the heading     \n\n"
                    "  This is the first line of text \n\n\n\n\n"
                    " There are too many new lines here    \n\n"
                    "   This one is good  \n\n\n"
                    "       This one is not")
        test = markdown_to_blocks(markdown)
        expected = ["# This is the heading", "This is the first line of text", "There are too many new lines here",
                    "This one is good", "This one is not"]
        self.assertEqual(test, expected)


if __name__ == "__main__":
    unittest.main()