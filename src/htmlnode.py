from __future__ import annotations
from typing import List, Dict, Optional, Union


class HTMLNode:
    def __init__(
        self,
        tag: Optional[str] = None,
        value: Optional[str] = None,
        children: Optional[List[HTMLNode]] = None,
        props: Optional[Dict] = None,
    ):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        if (self.value!=None) & (self.children!=None):
            raise ValueError("Cannot have both a value and children, they are mutually exclusive.")

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if not self.props:
            return ""
        html=""
        for prop, value in self.props.items():
            html += f' {prop}="{value}"'
        return html
    
    def __repr__(self):
        return f'HTMLNode("{self.tag}", "{self.value}", {self.children}, {self.props})'
    

class LeafNode(HTMLNode):
    def __init__(
        self,
        tag: Union[str,None],
        value: str,
        props: Optional[Dict] = None,
    ):
        super().__init__(
            tag=tag,
            value=value,
            props=props
        )
    
    def to_html(self):
        if not self.tag:
            return self.value
        if not self.value:
            raise ValueError("All leaf nodes _must_ have a value.")
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f'LeafNode("{self.tag}", "{self.value}", {self.props})'
    
    def __eq__(self, other: LeafNode):
        same_tag = (self.tag == other.tag)
        same_value = (self.value == other.value)
        same_props = (self.props == other.props)
        return same_tag & same_value & same_props


class ParentNode(HTMLNode):
    def __init__(
        self,
        tag: str,
        children: List[HTMLNode],
        props: Optional[Dict] = None,
    ):
        super().__init__(
            tag=tag,
            children=children,
            props=props,
        )
    
    def to_html(self):
        if not self.tag:
            raise ValueError("All parent nodes _must_ have a tag.")
        if not self.children or len(self.children)==0:
            raise ValueError("All parent nodes _must_ have children.")
        output = f"<{self.tag}{self.props_to_html()}>"
        for node in self.children:
            output += node.to_html()
        output += f"</{self.tag}>"
        return output
    
    def __repr__(self):
        return f'ParentNode("{self.tag}", {self.children}, {self.props})'
    
def main():
    node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank",})
    print(f"{node.props_to_html()=}")
    leaf = LeafNode("p","some string value", props={"somekey":"somevalue"})
    print(f"{leaf=}")
    parent = ParentNode("code",[leaf, leaf])
    print(f"{parent=}")
    
if __name__=="__main__":
    main()