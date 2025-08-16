import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from scripts.count.count_lang import count_lang_files
from count_original import count_md_files_in_original

from scripts.generate.count_notes import count_notes


if __name__ == "__main__":
    count_lang_files()
    count_md_files_in_original()
    count_notes()
