from __future__ import annotations
from typing import List, Dict, Optional


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
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
def main():
    x = HTMLNode(props={"href": "https://www.google.com", "target": "_blank",})
    print(x.props_to_html())
    
if __name__=="__main__":
    main()