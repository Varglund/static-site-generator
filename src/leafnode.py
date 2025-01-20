from htmlnode import HTMLNode
from typing import Union, Optional, Dict

class LeafNode(HTMLNode):
    def __init__(
        self,
        tag: Union[str,None],
        value: str,
        props: Optional[Dict] = None,
    ):
        super().__init__()
        
def main():
    x = LeafNode("p","some string value", props={"somekey":"somevalue"})
    print(x)
    
if __name__=="__main__":
    main()