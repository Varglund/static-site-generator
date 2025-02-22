from typing import List
from enum import Enum, auto

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def markdown_to_blocks(markdown:str)->List[str]:
    blocks = markdown.split(sep="\n\n")
    return [block.strip() for block in blocks if block != ""]

def block_to_block_type(block)->BlockType:
    heading = r"^#{1,6} (.*)$"
    code = r"^```(.*?)```$"
    quote = r"^>"
    unordered_list = r"^[*-] .*$"

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
        ordered_list = rf"^{ordinal}\. .*$"
        if not ordered_list.match(line):
            break
        ordinal += 1
    else:
        return BlockType.ORDERED_LIST
    
    return BlockType.PARAGRAPH
        