import unittest

from inline_markdown import *

class TestSplitNodes(unittest.TestCase):
    # def test_code(self):
    #     node = TextNode("This is text with a `code block` word", TextType.TEXT)
    #     new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    #     expected =[TextNode("This is text with a ", TextType.TEXT),
    #                TextNode("code block", TextType.CODE),
    #                TextNode(" word", TextType.TEXT)
    #                ]
    #     self.assertEqual(new_nodes, expected)
    #
    # def test_italic(self):
    #     node = TextNode("The words in *this phrase* are italicized", TextType.TEXT)
    #     new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
    #     expected = [TextNode("The words in ", TextType.TEXT),
    #                 TextNode("this phrase", TextType.ITALIC),
    #                 TextNode(" are italicized", TextType.TEXT)
    #                 ]
    #     self.assertEqual(new_nodes, expected)
    #
    # def test_bold(self):
    #     node = TextNode("The words in **this phrase** are bold", TextType.TEXT)
    #     new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    #     expected = [TextNode("The words in ", TextType.TEXT),
    #                 TextNode("this phrase", TextType.BOLD),
    #                 TextNode(" are bold", TextType.TEXT)
    #                 ]
    #     self.assertEqual(new_nodes, expected)
    #
    # def test_exception(self):
    #     node = TextNode("The words in **this phrase are bold", TextType.TEXT)
    #     with self.assertRaises(Exception) as context:
    #         new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    #
    # def test_not_textypeTEXT(self):
    #     node = TextNode("This is all code", TextType.CODE)
    #     new_nodes = split_nodes_delimiter([node], '`', TextType.CODE)
    #     expected = [TextNode("This is all code", TextType.CODE)]
    #     self.assertEqual(new_nodes, expected)
    #
    # def test_link(self):
    #     node = TextNode(
    #         "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
    #         TextType.TEXT,
    #     )
    #     new_nodes = split_nodes_link([node])
    #     expected = [
    #         TextNode("This is text with a link ", TextType.TEXT),
    #         TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
    #         TextNode(" and ", TextType.TEXT),
    #         TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev")
    #     ]
    #     self.assertEqual(new_nodes, expected)
    #
    # def test_image(self):
    #     node = TextNode(
    #         "This is a node with ![an image](www.image.com) embedded", TextType.TEXT
    #     )
    #     new_nodes = split_nodes_image([node])
    #     expected = [
    #         TextNode("This is a node with ", TextType.TEXT),
    #         TextNode("an image", TextType.IMAGE, "www.image.com"),
    #         TextNode(" embedded", TextType.TEXT)
    #     ]
    #     self.assertEqual(new_nodes, expected)

    # def test_text_to_textnode(self):
    #     text = ("This is **text** with an *italic* word and a `code block` and an ![obi wan image]"
    #             "(https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)")
    #     test = text_to_textnodes(text)
    #     expected = [
    #         TextNode("This is ", TextType.TEXT),
    #         TextNode("text", TextType.BOLD),
    #         TextNode(" with an ", TextType.TEXT),
    #         TextNode("italic", TextType.ITALIC),
    #         TextNode(" word and a ", TextType.TEXT),
    #         TextNode("code block", TextType.CODE),
    #         TextNode(" and an ", TextType.TEXT),
    #         TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
    #         TextNode(" and a ", TextType.TEXT),
    #         TextNode("link", TextType.LINK, "https://boot.dev"),
    #     ]
    #     self.assertEqual(test, expected)


if __name__ == "__main__":
    unittest.main()