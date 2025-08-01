import os

def count_notes():
    file_count = len([f for f in os.listdir('notes') if os.path.isfile(os.path.join('notes', f))])
    return file_count

print(count_notes())
