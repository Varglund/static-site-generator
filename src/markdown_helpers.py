from textnode import TextNode, TextType
from typing import List, Tuple, Optional
from enum import Enum
import re

class Delimiter(Enum):
    ITALIC = "*"
    BOLD = "**"
    CODE = "`"


def split_nodes_delimiter(old_nodes: List[TextNode], delimiter: Delimiter, text_type: TextType):
    if not old_nodes:
        raise ValueError("no nodes provided")
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL_TEXT:
            new_nodes.append(node)
            continue
        fragments = node.text.split(sep=delimiter.value, maxsplit=3)
        no_frags = len(fragments)
        if no_frags==3:
            new_nodes.extend([
                TextNode(fragments[0],TextType.NORMAL_TEXT),
                TextNode(fragments[1], text_type),
                TextNode(fragments[2],TextType.NORMAL_TEXT),
            ])
        elif no_frags == 1:
            new_nodes.append(node)
        else:
            raise ValueError(f"Text '{node.text}' only contained one copy of {delimiter.value=}")
    return new_nodes

def extract_markdown_images(text: str)->Optional[List[Tuple[str,str]]]:
    if not text:
        return None
    # pattern = re.compile(r"![rick roll](https://i.imgur.com/aKaOqIh.gif)")
    # pattern = re.compile(r"!\[(.*?)\]\((https?://w+\.w+\.w+/w+\.w+)\)")
    pattern = re.compile(r"!\[(.*?)\]\((https://.*?)\)")
    return re.findall(pattern, text)