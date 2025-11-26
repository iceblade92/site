import os

from copystatic import delete_dir, copy_files_recursive
from gencontent import generate_pages_recursive

def main():
    delete_dir()
    
    static_dir = "./static"
    public_dir = "./public"
    content_dir = "./content"
    template_dir = "./template.html"

    print("copying files to public")
    copy_files_recursive(static_dir, public_dir)

    print("generating pages")
    generate_pages_recursive(content_dir, template_dir, public_dir)

if __name__ == "__main__":
    main()
