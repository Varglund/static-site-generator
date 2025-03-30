from file_handling import copy_files_recursive, generate_page
import shutil
import os
import sys

def main():
    if len(sys.argv)==1:
        BASEPATH = "/"
    else:
        BASEPATH = sys.argv[1]
    if os.path.exists(os.path.join("docs")):
        shutil.rmtree(os.path.join("docs"))
    copy_files_recursive(os.path.join("static"), os.path.join("docs"), BASEPATH)
    copy_files_recursive(os.path.join("content"), os.path.join("docs"), BASEPATH)
    
if __name__ == '__main__':
    main()