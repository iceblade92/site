from copystatic import delete_dir, copy_files_recursive
from gencontent import generate_page

def main():
    delete_dir()
    copy_files_recursive("static", "public")
    from_path = "./content/index.md"
    template_path = "./template.html"
    dest_path = "./public/index.html"
    generate_page(from_path, template_path, dest_path)

if __name__ == "__main__":
    main()
