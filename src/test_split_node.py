import unittest

from textnode import TextNode, TextType
from split_node import split_nodes_delimiter, Delimiter, split_all_nodes

class TestSplitNode(unittest.TestCase):
    def test_split_code(self):
        node = TextNode("This is text with a `code block` word", TextType.NORMAL_TEXT)
        new_nodes = split_nodes_delimiter([node], Delimiter.CODE, TextType.CODE_TEXT)
        expected = [
            TextNode("This is text with a ", TextType.NORMAL_TEXT),
            TextNode("code block", TextType.CODE_TEXT),
            TextNode(" word", TextType.NORMAL_TEXT),
        ]
        self.assertEqual(new_nodes, expected)
    
    def test_split_italic(self):
        node = TextNode("This is text with an *italic block* word", TextType.NORMAL_TEXT)
        new_nodes = split_nodes_delimiter([node], Delimiter.ITALIC, TextType.ITALIC_TEXT)
        expected = [
            TextNode("This is text with an ", TextType.NORMAL_TEXT),
            TextNode("italic block", TextType.ITALIC_TEXT),
            TextNode(" word", TextType.NORMAL_TEXT),
        ]
        self.assertEqual(new_nodes, expected)
    
    def test_split_bold(self):
        node = TextNode("This is text with an **bold block** word", TextType.NORMAL_TEXT)
        new_nodes = split_nodes_delimiter([node], Delimiter.BOLD, TextType.BOLD_TEXT)
        expected = [
            TextNode("This is text with an ", TextType.NORMAL_TEXT),
            TextNode("bold block", TextType.BOLD_TEXT),
            TextNode(" word", TextType.NORMAL_TEXT),
        ]
        self.assertEqual(new_nodes, expected)
    
    def test_split_multiple_bold(self):
        node = TextNode("This is text with an **bold block** word", TextType.NORMAL_TEXT)
        new_nodes = split_nodes_delimiter([node, node, node], Delimiter.BOLD, TextType.BOLD_TEXT)
        expected = [
            TextNode("This is text with an ", TextType.NORMAL_TEXT),
            TextNode("bold block", TextType.BOLD_TEXT),
            TextNode(" word", TextType.NORMAL_TEXT),
            TextNode("This is text with an ", TextType.NORMAL_TEXT),
            TextNode("bold block", TextType.BOLD_TEXT),
            TextNode(" word", TextType.NORMAL_TEXT),
            TextNode("This is text with an ", TextType.NORMAL_TEXT),
            TextNode("bold block", TextType.BOLD_TEXT),
            TextNode(" word", TextType.NORMAL_TEXT),
        ]
        self.assertEqual(new_nodes, expected)
    
    def test_ignore_non_text_nodes(self):
        node = TextNode("This is text with an **bold block** word", TextType.BOLD_TEXT)
        new_nodes = split_nodes_delimiter([node], Delimiter.BOLD, TextType.BOLD_TEXT)
        expected = [node]
        self.assertEqual(new_nodes, expected)
    
    def test_delimiter_not_found_return_node(self):
        node = TextNode("This is text with a `code block` word", TextType.NORMAL_TEXT)
        new_nodes = split_nodes_delimiter([node], Delimiter.ITALIC, TextType.ITALIC_TEXT)
        expected = [node]
        self.assertEqual(new_nodes, expected)
        
    def test_only_one_delimiter_found_raise(self):
        with self.assertRaises(ValueError) as cm:
            node = TextNode("This is text with a poorly formatted *italic word", TextType.NORMAL_TEXT)
            split_nodes_delimiter([node], Delimiter.ITALIC, TextType.ITALIC_TEXT)
    
    # def test_split_multiple_bold(self):
    #     node = TextNode("This is text with **bold stuff**, *italics stuff*, and `code blocks` to separate out.", TextType.NORMAL_TEXT)
    #     new_nodes = split_nodes_delimiter([node, node, node], Delimiter.BOLD, TextType.BOLD_TEXT)
    #     expected = [
    #         TextNode("This is text with ", TextType.NORMAL_TEXT),
    #         TextNode("bold stuff", TextType.BOLD_TEXT),
    #         TextNode(", ", TextType.NORMAL_TEXT),
    #         TextNode("italics stuff", TextType.ITALIC_TEXT),
    #         TextNode(", and ", TextType.NORMAL_TEXT),
    #         TextNode("code blocks", TextType.CODE_TEXT),
    #         TextNode(" to separate out.", TextType.NORMAL_TEXT),
    #     ]
    #     self.assertEqual(new_nodes, expected)
            
            
        

if __name__ == '__main__':
    unittest.main()