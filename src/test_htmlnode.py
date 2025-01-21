import unittest

from htmlnode import HTMLNode

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


if __name__ == "__main__":
    unittest.main()
    