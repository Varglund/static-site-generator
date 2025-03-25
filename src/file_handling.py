import os
import shutil
import logging

logging.basicConfig(filename=os.path.join("logging","copy_logs.log"), level=logging.DEBUG)

def initialize_dir(dir_path:os.PathLike)->None:
    if os.path.exists(dir_path):
        shutil.rmtree(dir_path)
    os.mkdir(dir_path)

def recursive_copy(from_path:os.PathLike, to_path:os.PathLike)->None:
    if os.path.isfile(from_path):
        shutil.copy(from_path, to_path)
        return None
    elif not os.path.exists(from_path):
        raise ValueError(f"The directory {from_path=} does not exist.")
    logging.debug(f"Initializing {to_path=}")
    initialize_dir(to_path)
    for item in (contents:=os.listdir(from_path)):
        logging.debug(f"Handling {item} from {contents=}")
        logging.debug(f"Calling recursive copy on {os.path.join(from_path, item)} to {os.path.join(to_path, item)}.")
        recursive_copy(os.path.join(from_path, item), os.path.join(to_path, item))