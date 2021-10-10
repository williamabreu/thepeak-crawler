import os
from typing import List


def find_files(file_name: str, base_dir: str) -> List[str]:
    return [
        os.path.join(root, file_name)
        for root, subdirs, files in os.walk(base_dir)
        if root != base_dir and file_name in files
    ]
