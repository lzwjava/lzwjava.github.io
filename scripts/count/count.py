import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from count_py import count_py_in_script
from count_original import count_md_files_in_original

from scripts.generate.count_notes import count_notes


if __name__ == "__main__":
    count_py_in_script()
    count_md_files_in_original()
    count_notes()
