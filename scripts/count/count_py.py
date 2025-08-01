import os

def count_py_files(directory):
    count = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                count += 1
    return count

scripts_dir = '../'  # Go up one level from count/ to scripts/
py_count = count_py_files(scripts_dir)
print(f"Number of .py files in scripts directory: {py_count}")

