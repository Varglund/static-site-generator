import unittest
from block_markdown import (
    markdown_to_blocks
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

if __name__ == '__main__':
    unittest.main()