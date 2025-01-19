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
        
    def test__repr__(self):
        tag = "p"
        value = "Some kind of text which goes in a <p> tag in HTML."
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        node = HTMLNode(
            tag=tag,
            value=value,
            children=None,
            props=props
        )
        expected = f"HTMLNode({tag}, {value}, None, {props})"
        self.assertEqual(node, expected)
        
    def test_raise_if_both_value_and_children(self):
        self.assertRaises(
            ValueError,
            HTMLNode(value="something", children=[HTMLNode(tag="p")])
            )
        
if __name__ == '__main__':
    unittest.main()