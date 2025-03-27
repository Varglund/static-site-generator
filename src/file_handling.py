import os
import shutil
from block_markdown import markdown_to_html_node, extract_title

def generate_page(from_path, template_path, dest_path)->None:
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
    if not os.path.exists(os.path.join("public")):
        os.mkdir(os.path.join("public"))
    with open(dest_path, "w") as fp:
        fp.write(contents_html)
    return None

def copy_files_recursive(source_dir_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    for filename in os.listdir(source_dir_path):
        from_path = os.path.join(source_dir_path, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        print(f" * {from_path} -> {dest_path}")
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            copy_files_recursive(from_path, dest_path)