# import unittest
#
# from htmlnode import HTMLNode, LeafNode, ParentNode
#
# class TestHTMLNode(unittest.TestCase):
#     def test_props_to_html1(self):
#         node = HTMLNode("p", "This is a Test", children=None, props={"title": "Im a tooltip"})
#         expected = ' title="Im a tooltip"'
#         self.assertEqual(node.props_to_html(), expected)
#
#     def test_props_to_html2(self):
#         node = HTMLNode("img", "This is a Test", children=None, props={"src":"img.png", "width": "500","height": "600"})
#         expected = ' src="img.png" width="500" height="600"'
#         self.assertEqual(node.props_to_html(), expected)
#
#     def test_props_to_html3(self):
#         node = HTMLNode("a", "This is a Test", children=None, props={"href":"https://www.google.com", "target": "_blank"})
#         expected =  ' href="https://www.google.com" target="_blank"'
#         self.assertEqual(node.props_to_html(), expected)
#
#     def test_leaf_node1(self):
#         leaf = LeafNode("p", "Hello world").to_html()
#         expected = "<p>Hello world</p>"
#         self.assertEqual(leaf, expected)
#
#     def test_leaf_node2(self):
#         leaf = LeafNode("a", "Click me!", {"href": "https://www.google.com"}).to_html()
#         expected = '<a href="https://www.google.com">Click me!</a>'
#         self.assertEqual(leaf, expected)
#
#     def test_leaf_node3(self):
#         leaf = LeafNode(value="Just some text").to_html()
#         expected = "Just some text"
#         self.assertEqual(leaf, expected)
#
#     def test_no_value_raises_error(self):
#         leaf = LeafNode("p")
#         with self.assertRaisesRegex(ValueError, "LeafNode must have a value"):
#             leaf.to_html()
#
#     def test_parent_node1(self):
#         node = ParentNode(
#             "p",
#             [
#                 LeafNode("b", "Bold text"),
#                 LeafNode(None, "Normal text"),
#                 LeafNode("i", "italic text"),
#                 LeafNode(None, "Normal text"),
#             ],
#         ).to_html()
#         expectation = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
#         self.assertEqual(node, expectation)
#
#     def test_parent_node2(self):
#         node = ParentNode(
#         "div",
#     [
#                 LeafNode("b", "Bold text", {"class": "bold"}),
#                 LeafNode(None, "Normal text"),
#                 LeafNode("i", "italic text", {"id": "italic1"})
#             ],
#             {"class": "container"}
#         ).to_html()
#         expectation = '<div class="container"><b class="bold">Bold text</b>Normal text<i id="italic1">italic text</i></div>'
#         self.assertEqual(node, expectation)
#
#     # Test 1: Basic parent with leaf nodes
#     def test_basic_parent(self):
#         node = ParentNode(
#             "div",
#             [
#                 LeafNode("p", "Hello"),
#                 LeafNode("p", "World")
#             ]
#         ).to_html()
#         expected = '<div><p>Hello</p><p>World</p></div>'
#         self.assertEqual(node, expected)
#
#     # Test 2: Parent with props
#     def test_parent_with_props(self):
#         node = ParentNode(
#             "div",
#             [LeafNode("p", "Text")],
#             {"class": "wrapper", "id": "main"}
#         ).to_html()
#         expected = '<div class="wrapper" id="main"><p>Text</p></div>'
#         self.assertEqual(node, expected)
#
#     # Test 3: Nested parents
#     def test_nested_parents(self):
#         node = ParentNode(
#             "div",
#             [
#                 ParentNode(
#                     "section",
#                     [LeafNode("p", "Nested")]
#                 )
#             ]
#         ).to_html()
#         expected = '<div><section><p>Nested</p></section></div>'
#         self.assertEqual(node, expected)
#
#     # Test 4: Mixed nodes with props
#     def test_mixed_nodes(self):
#         node = ParentNode(
#             "article",
#             [
#                 LeafNode("h1", "Title", {"class": "title"}),
#                 LeafNode(None, "Plain text"),
#                 ParentNode(
#                     "div",
#                     [LeafNode("p", "More text")],
#                     {"class": "content"}
#                 )
#             ],
#             {"id": "article-1"}
#         ).to_html()
#         expected = '<article id="article-1"><h1 class="title">Title</h1>Plain text<div class="content"><p>More text</p></div></article>'
#         self.assertEqual(node, expected)
#
#     # Test 5: Error cases
#     def test_errors(self):
#         node = ParentNode(None, [LeafNode("p", "Text")])
#         with self.assertRaisesRegex(ValueError, "ParentNode must have tag"):
#             node.to_html()
#
#
# if __name__ == "__main__":
#     unittest.main()
