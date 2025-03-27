from file_handling import copy_files_recursive, generate_page
import shutil
import os

def main():
    if os.path.exists(os.path.join("public")):
        shutil.rmtree(os.path.join("public"))
    copy_files_recursive(os.path.join(os.path.abspath("."),"static"), os.path.join(os.path.abspath("."),"public"))
    generate_page(
        os.path.join("content","index.md"),
        os.path.join("template.html"),
        os.path.join("public","index.html")
        )
    
if __name__ == '__main__':
    main()