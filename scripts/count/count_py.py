import os


def count_py_files(directory):
    count = 0
    try:
        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)
            if os.path.isfile(item_path) and item.endswith(".py"):
                count += 1
            elif os.path.isdir(item_path):
                count += count_py_files(item_path)
    except PermissionError:
        pass
    return count


def count_py_in_script():
    scripts_dir = "../"  # Go up one level from count/ to scripts/
    py_count = count_py_files(scripts_dir)
    print(f"Number of .py files in scripts directory: {py_count}")


if __name__ == "__main__":
    count_py_in_script()
