import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

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

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )
        
if __name__ == '__main__':
    unittest.main()