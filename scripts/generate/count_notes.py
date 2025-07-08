import os
file_count = len([f for f in os.listdir('notes') if os.path.isfile(os.path.join('notes', f))])
print(file_count)