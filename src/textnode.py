from enum import Enum

class TextType(Enum):
    NORMAL_TEXT = "normal_text"
    BOLD_TEXT = "bold_text"
    ITALIC_TEXT = "italic_text"
    CODE_TEXT = "code_text"
    LINK = "link"
    IMAGE = "image"