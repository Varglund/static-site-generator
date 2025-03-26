from typing import List
from enum import Enum
from inline_markdown import text_to_textnodes
from htmlnode import ParentNode
from textnode import text_node_to_html_node, TextNode, TextType
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def extract_title(markdown:str)->str:
    markdown_blocks = markdown_to_blocks(markdown)
    block_types = list(map(block_to_block_type, markdown_blocks))
    blocks_and_types = list(zip(markdown_blocks, block_types))
    headings = [block for block, type in blocks_and_types if type == BlockType.HEADING]
    html_heading_nodes = list(map(heading_to_html_node,headings))
    h1_nodes = [node for node in html_heading_nodes if node.tag == "h1"]
    print(h1_nodes)
    title = h1_nodes[0].children[0].value
    print(title)
    return title

def markdown_to_blocks(markdown:str)->List[str]:
    blocks = markdown.split(sep="\n\n")
    return [block.strip() for block in blocks if block != ""]

def block_to_block_type(block)->BlockType:
    heading = re.compile(r"^#{1,6} (.*)$")
    code = re.compile(r"^```(.*?)```$")
    quote = re.compile(r"^>")
    unordered_list = re.compile(r"^[*-] .*$")

    if heading.match(block):
        return BlockType.HEADING
    if code.match(block):
        return BlockType.CODE
    
    lines = block.split("\n")
    
    for line in lines:
        if not quote.match(line):
            break
    else:
        return BlockType.QUOTE
    
    for line in lines:
        if not unordered_list.match(line):
            break
    else:
        return BlockType.UNORDERED_LIST
    
    for line in lines:
        if not unordered_list.match(line):
            break
    else:
        return BlockType.UNORDERED_LIST
    
    ordinal = 1
    for line in lines:
        ordered_list = re.compile(rf"^{ordinal}\. .*$")
        if not ordered_list.match(line):
            break
        ordinal += 1
    else:
        return BlockType.ORDERED_LIST
    
    return BlockType.PARAGRAPH

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children, None)

def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == BlockType.PARAGRAPH:
        return paragraph_to_html_node(block)
    if block_type == BlockType.HEADING:
        return heading_to_html_node(block)
    if block_type == BlockType.CODE:
        return code_to_html_node(block)
    if block_type == BlockType.OLIST:
        return olist_to_html_node(block)
    if block_type == BlockType.ULIST:
        return ulist_to_html_node(block)
    if block_type == BlockType.QUOTE:
        return quote_to_html_node(block)
    raise ValueError("invalid block type")

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children

def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)

def heading_to_html_node(block):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    if level + 1 >= len(block):
        raise ValueError(f"invalid heading level: {level}")
    text = block[level + 1 :]
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)

def code_to_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("invalid code block")
    text = block[4:-3]
    raw_text_node = TextNode(text, TextType.TEXT)
    child = text_node_to_html_node(raw_text_node)
    code = ParentNode("code", [child])
    return ParentNode("pre", [code])


def olist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[3:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)


def ulist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)


def quote_to_html_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)



if __name__=="__main__":
    extract_title("""some plain text before a \n\n- bulleted\ni-list\n\n## H2 before title?\n\n# Title""")