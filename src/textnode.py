from __future__ import annotations
from enum import Enum
from typing import Optional

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
    
