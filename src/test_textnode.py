import unittest

from textnode import TextNode, TextType

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
        
if __name__ == '__main__':
    unittest.main()