import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        reference = ' href="https://www.google.com" target="_blank"'
        node = HTMLNode(props=props)
        self.assertEqual(node.props_to_html(), reference)
        
    def test_props_to_html_is_none(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")
        
    def test_raise_if_both_value_and_children(self):
        with self.assertRaises(ValueError) as cm:
            HTMLNode(value="something", children=[HTMLNode(tag="p")])
        
    def test_to_html_not_implemented(self):
        node = HTMLNode()
        with self.assertRaises(NotImplementedError) as cm:
            node.to_html()
        
if __name__ == '__main__':
    unittest.main()