from htmlnode import HTMLNode
from leafnode import LeafNode
from typing import Optional, Dict, List

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
        
def main():
    x = LeafNode("p","some string value", props={"somekey":"somevalue"})
    print(x)
    
if __name__=="__main__":
    main()