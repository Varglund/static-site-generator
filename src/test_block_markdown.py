import unittest
from block_markdown import (
    markdown_to_blocks,
    block_to_block_type,
    BlockType
)

class TestBlockMarkdown(unittest.TestCase):
    
    def test_markdown_to_blocks(self)->None:
        markdown = (
"""# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""
            )
        actual = markdown_to_blocks(markdown)
        expected = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
"""* This is the first list item in a list block
* This is a list item
* This is another list item"""
        ]
        self.assertEqual(actual, expected)
    
    def test_markdown_to_blocks_with_excessive_whitespace(self)->None:
        markdown = (
"""# This is a heading



This is a paragraph of text. It has some **bold** and *italic* words inside of it.



* This is the first list item in a list block
* This is a list item
* This is another list item"""
            )
        actual = markdown_to_blocks(markdown)
        expected = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
"""* This is the first list item in a list block
* This is a list item
* This is another list item"""
        ]
        self.assertEqual(actual, expected)


def test_block_to_block_types(self):
    block = "# heading"
    self.assertEqual(block_to_block_type(block), BlockType.HEADING)
    block = "```\ncode\n```"
    self.assertEqual(block_to_block_type(block), BlockType.CODE)
    block = "> quote\n> more quote"
    self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
    block = "* list\n* items"
    self.assertEqual(block_to_block_type(block), BlockType.ULIST)
    block = "1. list\n2. items"
    self.assertEqual(block_to_block_type(block), BlockType.OLIST)
    block = "paragraph"
    self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)


if __name__ == '__main__':
    unittest.main()