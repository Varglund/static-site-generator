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
    # pattern = re.compile(r"!\[(.*?)\]\((https://.*?)\)")  # mine
    pattern = re.compile(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)")  # boot.dev
    return pattern.findall(text)

def extract_markdown_links(text: str)->Optional[List[Tuple[str,str]]]:
    if not text:
        return None
    # pattern = re.compile(r"\[(.*?)\]\((https://.*?)\)")  # mine
    pattern = re.compile(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)")  # boot.dev
    return pattern.findall(text)

def split_nodes_link(old_nodes: List[TextNode]):
    if not old_nodes:
        raise ValueError("no nodes provided")
    new_nodes = []
    for node in old_nodes:
        line = node.text
        links = extract_markdown_links(node.text)
        if not links:
            new_nodes.append(node)
            continue
        for link in links: 
            start = line.index(link[0]) -1
            end = line.index(link[1]) + len(link[1])
            if start==0:
                new_nodes.extend([
                    TextNode(link[0], TextType.LINK, link[1]),
                ])
            else:
                new_nodes.extend([
                    TextNode(line[:start],TextType.NORMAL_TEXT),
                    TextNode(link[0], TextType.LINK, link[1]),
                ])
            if (end+1)<len(line):
                line = line[end+1:]
            else:
                line = ""
        else:
            if line:
                new_nodes.append(
                    TextNode(line,TextType.NORMAL_TEXT)
                )
    return new_nodes

def split_nodes_image(old_nodes: List[TextNode]):
    if not old_nodes:
        raise ValueError("no nodes provided")
    new_nodes = []
    for node in old_nodes:
        line = node.text
        images = extract_markdown_images(node.text)
        if not images:
            new_nodes.append(node)
            continue
        for image in images: 
            start = line.index(image[0]) - 2
            end = line.index(image[1]) + len(image[1])
            if start==0:
                new_nodes.extend([
                    TextNode(image[0], TextType.IMAGE, image[1]),
                ])
            else:
                new_nodes.extend([
                    TextNode(line[:start],TextType.NORMAL_TEXT),
                    TextNode(image[0], TextType.IMAGE, image[1]),
                ])
            if (end+1)<len(line):
                line = line[end+1:]
            else:
                line = ""
        else:
            if line:
                new_nodes.append(
                    TextNode(line,TextType.NORMAL_TEXT)
                )
    return new_nodes