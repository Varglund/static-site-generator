from __future__ import annotations
from htmlnode import HTMLNode
from typing import Union, Optional, Dict

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
        if not self.value:
            raise ValueError("All leaf nodes _must_ have a value.")
        if not self.tag:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f'LeafNode("{self.tag}", "{self.value}", {self.props})'
    
    def __eq__(self, other: LeafNode):
        same_tag = (self.tag == other.tag)
        same_value = (self.value == other.value)
        same_props = (self.props == other.props)
        return same_tag & same_value & same_props
        
def main():
    x = LeafNode("p","some string value", props={"somekey":"somevalue"})
    print(x)
    
if __name__=="__main__":
    main()