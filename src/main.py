from textnode import TextNode, TextType

def main():
    dummy = TextNode("My name is chica chica Slim Shady", TextType.NORMAL_TEXT, "https://www.youtube.com/watch?v=QWcfbZPf2gk")
    print(dummy)
    
if __name__ == '__main__':
    main()