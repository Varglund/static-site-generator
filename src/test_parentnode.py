import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_init_takes_no_value(self):
        with self.assertRaises(TypeError) as cm:
            ParentNode(tag="p", value="Some string value.", children=["some child"], props=None)
        
    def test_to_html_no_value(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        expected = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        actual = node.to_html()
        self.assertEqual(actual,expected)
        
    def test_to_html_with_nested_ParentNodes(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                ParentNode("p", [
                    LeafNode(None, "Normal text"),
                    LeafNode("i", "italic text"),
                    LeafNode(None, "Normal text"),
                ], props = {"prop_key":"prop_value"}),
                LeafNode(None, "Near closing normal text"),
                LeafNode("b", "Closing bold text"),
                
            ],
        )
        expected = '<p><b>Bold text</b><p prop_key="prop_value">Normal text<i>italic text</i>Normal text</p>Near closing normal text<b>Closing bold text</b></p>'
        actual = node.to_html()
        self.assertEqual(actual,expected)
    
    def test_to_html_with_props(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text", props={"prop1":"value1"}),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text", props={"prop2":"value2"}),
                LeafNode(None, "Normal text"),
            ],
        )
        expected = '<p><b prop1="value1">Bold text</b>Normal text<i prop2="value2">italic text</i>Normal text</p>'
        actual = node.to_html()
        self.assertEqual(actual,expected)
    
    def test_to_html_fails_without_children(self):
        node = ParentNode(
            "p",
            [],
        )
        with self.assertRaises(ValueError) as cm:
            node.to_html()
    
    def test_to_html_fails_without_a_tag(self):
        node = ParentNode(
            None,
            [LeafNode("p","Some paragraph text.")],
        )
        with self.assertRaises(ValueError) as cm:
            node.to_html()
        
if __name__ == '__main__':
    unittest.main()