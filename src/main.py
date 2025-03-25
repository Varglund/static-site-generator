from file_handling import recursive_copy
import os

def main():
    recursive_copy(os.path.join(os.path.abspath("."),"static"), os.path.join(os.path.abspath("."),"public"))
    
if __name__ == '__main__':
    main()