import os

from blocknode import markdown_to_html_node

def extract_title(markdown):
    lines = markdown.splitlines()

    for line in lines:
        if line.startswith("# "):
            title = line[2:].strip()
            return title
    raise Exception("No h1 header found")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as f:
        markdown_content_from = f.read()
    with open(template_path, "r") as f:
        markdown_content_template = f.read()
    node = markdown_to_html_node(markdown_content_from)
    html_content = node.to_html()
    title = extract_title(markdown_content_from)
    template = markdown_content_template
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html_content)
    dest_dir = os.path.dirname(dest_path)
    if dest_dir != "":
        os.makedirs(dest_dir, exist_ok=True)
    with open(dest_path, "w") as f:
        f.write(template)
    

