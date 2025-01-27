import unittest

from split_delimiter import *

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected =[TextNode("This is text with a ", TextType.TEXT),
                   TextNode("code block", TextType.CODE),
                   TextNode(" word", TextType.TEXT)
                   ]
        self.assertEqual(new_nodes, expected)

    def test_italic(self):
        node = TextNode("The words in *this phrase* are italicized", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        expected = [TextNode("The words in ", TextType.TEXT),
                    TextNode("this phrase", TextType.ITALIC),
                    TextNode(" are italicized", TextType.TEXT)
                    ]
        self.assertEqual(new_nodes, expected)

    def test_bold(self):
        node = TextNode("The words in **this phrase** are bold", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [TextNode("The words in ", TextType.TEXT),
                    TextNode("this phrase", TextType.BOLD),
                    TextNode(" are bold", TextType.TEXT)
                    ]
        self.assertEqual(new_nodes, expected)

    def test_exception(self):
        node = TextNode("The words in **this phrase are bold", TextType.TEXT)
        with self.assertRaises(Exception) as context:
            new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)

    def test_not_textypeTEXT(self):
        node = TextNode("This is all code", TextType.CODE)
        new_nodes = split_nodes_delimiter([node], '`', TextType.CODE)
        expected = [TextNode("This is all code", TextType.CODE)]
        self.assertEqual(new_nodes, expected)



if __name__ == "__main__":
    unittest.main()