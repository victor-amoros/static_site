from textnode import *
from htmlnode import *

def main():
    test = TextNode("test text", TextType.BOLD, "https://www.boot.dev")
    print(test)

main()