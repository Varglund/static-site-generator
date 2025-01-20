import unittest

from leafnode import LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_init_takes_no_children(self):
        with self.assertRaises(TypeError) as cm:
            LeafNode(tag="p", value="Some string value.", children=[LeafNode(value="this will fail")], props=None)
        
    def test_to_html_no_value(self):
        leaf = LeafNode(
            tag=None,
            value="",
            props=None
        )
        with self.assertRaises(ValueError) as cm:
            leaf.to_html()
    
    def test_to_html_no_tag(self):
        expected = "This is the value of the leaf."
        leaf = LeafNode(
            tag=None,
            value=expected,
            props=None
        )
        result = leaf.to_html()
        self.assertEqual(result, expected)
    
    def test_to_html_no_props(self):
        leaf = LeafNode(
            tag="p",
            value="This is a paragraph of text.",
            props=None
        )
        expected = "<p>This is a paragraph of text.</p>"
        result = leaf.to_html()
        self.assertEqual(result, expected)
    
    def test_to_html_one_prop(self):
        leaf = LeafNode(
            tag="a",
            value="Click me!",
            props={"href":"https://www.google.com"}
        )
        expected = '<a href="https://www.google.com">Click me!</a>'
        result = leaf.to_html()
        self.assertEqual(result, expected)
    
    def test_to_html_two_prop(self):
        leaf = LeafNode(
            tag="a",
            value="Click me!",
            props={"href":"https://www.google.com","prop2":"some_value"}
        )
        expected = '<a href="https://www.google.com" prop2="some_value">Click me!</a>'
        result = leaf.to_html()
        self.assertEqual(result, expected)
        
        
if __name__ == '__main__':
    unittest.main()