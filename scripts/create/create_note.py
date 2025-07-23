import os
import subprocess

from create_note_from_clipboard import create_note

def gpa():
    # Load bash profile to ensure environment variables are available
    command = "bash -l -c 'python ~/bin/gitmessageai.py --api deepseek --allow-pull-push'"
    subprocess.run(command, shell=True)

if __name__ == "__main__":
    create_note()
    # Call gpa function
    gpa()
