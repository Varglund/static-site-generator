from file_handling import copy_files_recursive, generate_page
import shutil
import os
import sys

def main():
    if len(sys.argv)==1:
        BASEPATH = "/"
    else:
        BASEPATH = sys.argv[1]
    if os.path.exists(os.path.join(BASEPATH,"public")):
        shutil.rmtree(os.path.join(BASEPATH,"public"))
    copy_files_recursive(os.path.join(BASEPATH,"static"), os.path.join(BASEPATH,"public"), BASEPATH)
    copy_files_recursive(os.path.join(BASEPATH,"content"), os.path.join(BASEPATH,"public"), BASEPATH)
    os.path.split()
    
if __name__ == '__main__':
    main()