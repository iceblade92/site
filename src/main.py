from textnode import TextNode, TextType
from copystatic import delete_dir, copy_files_recursive

def main():
    node = TextNode("hello world", TextType.TEXT)
    print(node)
    delete_dir()
    copy_files_recursive("static", "public")

if __name__ == "__main__":
    main()
