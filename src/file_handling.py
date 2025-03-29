import os
import shutil
from block_markdown import markdown_to_html_node, extract_title

TEMPLATE_PATH = os.path.join(os.path.relpath("."),"template.html")

def generate_page(from_path, template_path, dest_path, BASEPATH: str)->None:
    print(f"Generating page from {from_path} to {dest_path} using {template_path}.")
    with open(from_path) as fp:
        contents = fp.read()
    with open(template_path) as fp:
        template = fp.read()
    title = extract_title(contents)
    contents_html = markdown_to_html_node(contents).to_html()
    contents_html= (template
                    .replace("{{ Title }}", title)
                    .replace("{{ Content }}", contents_html)
                    )
    contents_html = (contents_html
                     .replace('href="/',f'href="{BASEPATH}')
                     .replace('src="/',f'src="{BASEPATH}'))
    dest_dir_path = os.path.join("public")
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    with open(dest_path, "w") as fp:
        fp.write(contents_html)
    return None

def copy_files_recursive(source_dir_path, dest_dir_path, BASEPATH):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    for filename in os.listdir(source_dir_path):
        from_path = os.path.join(source_dir_path, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        print(f" * {from_path} -> {dest_path}")
        if not os.path.isfile(from_path):
            copy_files_recursive(from_path, dest_path, BASEPATH)
        elif from_path.endswith(".md"):
            generate_page(from_path, TEMPLATE_PATH, dest_path.replace(".md",".html"), BASEPATH)
        else:
            shutil.copy(from_path,dest_path)