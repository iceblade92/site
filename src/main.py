import sys

from copystatic import delete_dir, copy_files_recursive
from gencontent import generate_pages_recursive

def main():
    delete_dir()
    
    if len(sys.argv) < 2:
        basepath = "/"
    else:
        basepath = sys.argv[1]
    static_dir = "./static"
    public_dir = "./docs"
    content_dir = "./content"
    template_dir = "./template.html"

    print("copying files to docs")
    copy_files_recursive(static_dir, public_dir)

    print("generating pages")
    generate_pages_recursive(content_dir, template_dir, public_dir, basepath)

if __name__ == "__main__":
    main()
