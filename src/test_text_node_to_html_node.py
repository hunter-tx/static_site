# test/test_text_node_to_html_node.py

import unittest
from textnode import TextNode, TextType
from htmlnode import LeafNode
from inline_markdown import text_node_to_html_node

class TestTextNodeToHtmlNode(unittest.TestCase):
    def test_basic_text(self):
        # Basic text
        node = TextNode("Hello", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertIsNone(html_node.tag)
        self.assertEqual(html_node.value, "Hello")
        self.assertEqual(html_node.props, {})

    def test_code_text(self):
        # Code
        node = TextNode("print('hi')", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "print('hi')")
        self.assertEqual(html_node.props, {})

    def test_link(self):
        # Link
        node = TextNode("Boot.dev", TextType.LINK, "https://boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Boot.dev")
        self.assertEqual(html_node.props, {"href": "https://boot.dev"})

    def test_image(self):
        # Image
        node = TextNode("Boot.dev Logo", TextType.IMAGE, "https://boot.dev/logo.png")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "https://boot.dev/logo.png", "alt": "Boot.dev Logo"})

    def test_error(self):
        # Invalid type test
        with self.assertRaises(ValueError):
            invalid_node = TextNode("test", "invalid")
