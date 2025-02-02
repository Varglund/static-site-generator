import unittest

from textnode import TextNode, TextType
from markdown_helpers import (
    split_nodes_delimiter,
    Delimiter,
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_link,
    split_nodes_image,
    text_to_textnodes,
)

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
    
    def test_extract_markdown_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        output = extract_markdown_images(text)
        expected = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(output, expected)
    
    def test_extract_markdown_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        output = extract_markdown_links(text)
        expected = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        self.assertEqual(output, expected)
        
    def test_split_nodes_link(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev)",
            TextType.NORMAL_TEXT,
        )
        new_nodes = split_nodes_link([node])
        expected =  [
            TextNode("This is text with a link ", TextType.NORMAL_TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
        ]
        self.assertEqual(new_nodes, expected)
    
    def test_split_nodes_beginning_link(self):
        node = TextNode(
            "[To boot dev](https://www.boot.dev) is text with a link ",
            TextType.NORMAL_TEXT,
        )
        new_nodes = split_nodes_link([node])
        expected =  [
            TextNode("To boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" is text with a link ", TextType.NORMAL_TEXT),
        ]
        self.assertEqual(new_nodes, expected)
    
    def test_split_nodes_only_link(self):
        node = TextNode(
            "[to boot dev](https://www.boot.dev)",
            TextType.NORMAL_TEXT,
        )
        new_nodes = split_nodes_link([node])
        expected =  [
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
        ]
        self.assertEqual(new_nodes, expected)
    
    def test_split_nodes_link_with_trailing_text(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and something at the end.",
            TextType.NORMAL_TEXT,
        )
        new_nodes = split_nodes_link([node])
        expected =  [
            TextNode("This is text with a link ", TextType.NORMAL_TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and something at the end.", TextType.NORMAL_TEXT),
        ]
        self.assertEqual(new_nodes, expected)
    
    def test_split_nodes_multiple_links(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.NORMAL_TEXT,
        )
        new_nodes = split_nodes_link([node])
        expected =  [
            TextNode("This is text with a link ", TextType.NORMAL_TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.NORMAL_TEXT),
            TextNode(
                "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
            ),
        ]
        self.assertEqual(new_nodes, expected)
        
    def test_split_nodes_multiple_links_with_trailing_text(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev) and an end.",
            TextType.NORMAL_TEXT,
        )
        new_nodes = split_nodes_link([node])
        expected =  [
            TextNode("This is text with a link ", TextType.NORMAL_TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.NORMAL_TEXT),
            TextNode(
                "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
            ),
            TextNode(" and an end.", TextType.NORMAL_TEXT),
        ]
        self.assertEqual(new_nodes, expected)
        
    def test_split_nodes_image(self):
        node = TextNode(
            "This is text with an image ![rick roll](https://i.imgur.com/aKaOqIh.gif)",
            TextType.NORMAL_TEXT,
        )
        new_nodes = split_nodes_image([node])
        expected =  [
            TextNode("This is text with an image ", TextType.NORMAL_TEXT),
            TextNode("rick roll", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"),
        ]
        self.assertEqual(new_nodes, expected)
    
    def test_split_nodes_beginning_image(self):
        node = TextNode(
            "![rick roll](https://i.imgur.com/aKaOqIh.gif) is text with an image.",
            TextType.NORMAL_TEXT,
        )
        new_nodes = split_nodes_image([node])
        expected =  [
            TextNode("rick roll", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"),
            TextNode(" is text with an image.", TextType.NORMAL_TEXT),
        ]
        self.assertEqual(new_nodes, expected)
    
    def test_split_nodes_only_image(self):
        node = TextNode(
            "![rick roll](https://i.imgur.com/aKaOqIh.gif)",
            TextType.NORMAL_TEXT,
        )
        new_nodes = split_nodes_image([node])
        expected =  [
            TextNode("rick roll", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"),
        ]
        self.assertEqual(new_nodes, expected)
    
    def test_split_nodes_image_with_trailing_text(self):
        node = TextNode(
            "This is text with an image ![rick roll](https://i.imgur.com/aKaOqIh.gif) and something at the end.",
            TextType.NORMAL_TEXT,
        )
        new_nodes = split_nodes_image([node])
        expected =  [
            TextNode("This is text with an image ", TextType.NORMAL_TEXT),
            TextNode("rick roll", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"),
            TextNode(" and something at the end.", TextType.NORMAL_TEXT),
        ]
        self.assertEqual(new_nodes, expected)
    
    def test_split_nodes_multiple_images(self):
        node = TextNode(
            "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)",
            TextType.NORMAL_TEXT,
        )
        new_nodes = split_nodes_image([node])
        expected =  [
            TextNode("This is text with a ", TextType.NORMAL_TEXT),
            TextNode("rick roll", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"),
            TextNode(" and ", TextType.NORMAL_TEXT),
            TextNode("obi wan", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
        ]
        self.assertEqual(new_nodes, expected)
        
    def test_split_nodes_multiple_images_with_trailing_text(self):
        node = TextNode(
            "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg) and an end.",
            TextType.NORMAL_TEXT,
        )
        new_nodes = split_nodes_image([node])
        expected =  [
            TextNode("This is text with a ", TextType.NORMAL_TEXT),
            TextNode("rick roll", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"),
            TextNode(" and ", TextType.NORMAL_TEXT),
            TextNode("obi wan", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and an end.", TextType.NORMAL_TEXT),
        ]
        self.assertEqual(new_nodes, expected)

    def test_text_to_textnodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        expected =  [
            TextNode("This is ", TextType.NORMAL_TEXT),
            TextNode("text", TextType.BOLD_TEXT),
            TextNode(" with an ", TextType.NORMAL_TEXT),
            TextNode("italic", TextType.ITALIC_TEXT),
            TextNode(" word and a ", TextType.NORMAL_TEXT),
            TextNode("code block", TextType.CODE_TEXT),
            TextNode(" and an ", TextType.NORMAL_TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.NORMAL_TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        self.assertEqual(nodes, expected)


if __name__ == '__main__':
    unittest.main()
