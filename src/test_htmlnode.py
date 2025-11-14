import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


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

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_empty_children(self):
        parent = ParentNode("div", [])
        self.assertEqual(parent.to_html(), "<div></div>")

    def test_to_html_missing_children_raises(self):
        parent = ParentNode("div", None)
        with self.assertRaisesRegex(ValueError, "must have a child"):
            parent.to_html()

    def test_missing_tag_raises(self):
        parent = ParentNode(None, [])
        with self.assertRaisesRegex(ValueError, "must have a tag"):
            parent.to_html()

    def test_parent_with_props(self):
        child = LeafNode("span", "child")
        parent = ParentNode("div", [child], {"class": "box", "id": "x"})
        self.assertEqual(parent.to_html(), '<div class="box" id="x"><span>child</span></div>')

if __name__ == "__main__":
    unittest.main()