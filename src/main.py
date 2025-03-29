from file_handling import copy_files_recursive, generate_page
import shutil
import os

def main():
    if os.path.exists(os.path.join("public")):
        shutil.rmtree(os.path.join("public"))
    copy_files_recursive(os.path.join(os.path.relpath("."),"static"), os.path.join(os.path.relpath("."),"public"))
    
if __name__ == '__main__':
    main()