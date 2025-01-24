from textnode import TextNode, TextType
from typing import List
from enum import Enum

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

def split_all_nodes(old_nodes: List[TextNode])->List[TextNode]:
    bolds = split_nodes_delimiter(old_nodes, Delimiter.BOLD, TextType.BOLD_TEXT)
    italics = split_nodes_delimiter(bolds, Delimiter.ITALIC, TextType.ITALIC_TEXT)
    codes = split_nodes_delimiter(italics, Delimiter.CODE, TextType.CODE_TEXT)
    return codes