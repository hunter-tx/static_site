import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html1(self):
        node = HTMLNode("p", "This is a Test", children=None, props={"title": "Im a tooltip"})
        expected = ' title="Im a tooltip"'
        self.assertEqual(node.props_to_html(), expected)

    def test_props_to_html2(self):
        node = HTMLNode("img", "This is a Test", children=None, props={"src":"img.png", "width": "500","height": "600"})
        expected = ' src="img.png" width="500" height="600"'
        self.assertEqual(node.props_to_html(), expected)

    def test_props_to_html3(self):
        node = HTMLNode("a", "This is a Test", children=None, props={"href":"https://www.google.com", "target": "_blank"})
        expected =  ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected)

    def test_leaf_node1(self):
        leaf = LeafNode("p", "Hello world").to_html()
        expected = "<p>Hello world</p>"
        self.assertEqual(leaf, expected)

    def test_leaf_node2(self):
        leaf = LeafNode("a", "Click me!", {"href": "https://www.google.com"}).to_html()
        expected = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(leaf, expected)

    def test_leaf_node3(self):
        leaf = LeafNode(value="Just some text").to_html()
        expected = "Just some text"
        self.assertEqual(leaf, expected)

    def test_no_value_raises_error(self):
        leaf = LeafNode("p")
        with self.assertRaisesRegex(ValueError, "LeafNode must have a value"):
            leaf.to_html()



if __name__ == "__main__":
    unittest.main()
