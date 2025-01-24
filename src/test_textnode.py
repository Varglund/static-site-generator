import unittest

from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import LeafNode
 
class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        other_node = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node, other_node)
    
    def test_url_not_eq(self):
        node = TextNode("This is a link node", TextType.LINK, url=None)
        other_node = TextNode("This is a link node", TextType.LINK, url="https://www.boot.dev/")
        self.assertNotEqual(node, other_node)
    
    def test_text_not_eq(self):
        node = TextNode("This is a link node", TextType.ITALIC_TEXT)
        other_node = TextNode("This is something else entirely", TextType.ITALIC_TEXT)
        self.assertNotEqual(node, other_node)
    
    def test_text_type_not_eq(self):
        node = TextNode("```This is code.```", TextType.CODE_TEXT)
        other_node = TextNode("```This is code.```", TextType.IMAGE)
        self.assertNotEqual(node, other_node)
    
    def test_repr(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(repr(node), "TextNode(This is a text node, bold_text, None)")
        
        
class TestTextNodeToHtmlNode(unittest.TestCase):
    def test_case_normal_text(self):
        tag = None
        text = "Some text"
        props = None
        node = TextNode(
            text=text,
            text_type=TextType.NORMAL_TEXT,
            url=None
        )
        expected = LeafNode(
            tag=tag, 
            value=text, 
            props=props
        )
        result = text_node_to_html_node(node)
        self.assertEqual(result, expected)
    
    def test_case_bold_text(self):
        tag = "b"
        text = "Some text"
        props = None
        node = TextNode(
            text=text,
            text_type=TextType.BOLD_TEXT,
            url=None
        )
        expected = LeafNode(
            tag=tag, 
            value=text, 
            props=props
        )
        result = text_node_to_html_node(node)
        self.assertEqual(result, expected)
    
    def test_case_italic_text(self):
        tag = "i"
        text = "Some text"
        props = None
        node = TextNode(
            text=text,
            text_type=TextType.ITALIC_TEXT,
            url=None
        )
        expected = LeafNode(
            tag=tag, 
            value=text, 
            props=props
        )
        result = text_node_to_html_node(node)
        self.assertEqual(result, expected)
    
    def test_case_code_text(self):
        tag = "code"
        text = "Some text"
        props = None
        node = TextNode(
            text=text,
            text_type=TextType.CODE_TEXT,
            url=None
        )
        expected = LeafNode(
            tag=tag, 
            value=text,
            props=props
        )
        result = text_node_to_html_node(node)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()