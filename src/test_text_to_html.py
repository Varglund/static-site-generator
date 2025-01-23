import unittest

from text_to_html import text_node_to_html_node
from textnode import TextNode, TextType
from leafnode import LeafNode

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
    