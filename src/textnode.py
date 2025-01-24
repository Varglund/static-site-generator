from __future__ import annotations
from enum import Enum
from typing import Optional
from htmlnode import LeafNode

class TextType(Enum):
    NORMAL_TEXT = "normal_text"
    BOLD_TEXT = "bold_text"
    ITALIC_TEXT = "italic_text"
    CODE_TEXT = "code_text"
    LINK = "link"
    IMAGE = "image"
    
class TextNode():
    def __init__(self, text: str, text_type: TextType, url: Optional[str] = None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other: TextNode):
        same_text = (self.text == other.text)
        same_text_type = (self.text_type == other.text_type)
        same_url = (self.url == other.url)
        return same_text & same_text_type & same_url
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
def text_node_to_html_node(text_node: TextNode):
    match text_node.text_type:
        case TextType.NORMAL_TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD_TEXT:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC_TEXT:
            return LeafNode("i", text_node.text)
        case TextType.CODE_TEXT:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, props={"href":text_node.url})
        case TextType.IMAGE:
            return LeafNode("img", "", props={"src":text_node.url, "alt":"Some image."})
        case _:
            raise ValueError(f"Incompatible text type of the node {text_node}")
