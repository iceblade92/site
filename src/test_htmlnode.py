import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        result = node.props_to_html()
        self.assertEqual(result, ' href="https://www.google.com" target="_blank"')

    def test_props_empty(self):
        node = HTMLNode()
        result = node.props_to_html()
        self.assertEqual(result, "")

    def test_tag(self):
        node = HTMLNode(tag="p")
        self.assertEqual(node.tag, "p")

    def test_value(self):
        node = HTMLNode(value="Hello World")
        self.assertEqual(node.value, "Hello World")

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_no_props(self):
        node = LeafNode("p", "")
        self.assertEqual(node.to_html(), "<p></p>")
    
    def test_leaf_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_leaf_value_error(self):
        with self.assertRaises(ValueError):
            LeafNode("p", None).to_html()

if __name__ == "__main__":
    unittest.main()