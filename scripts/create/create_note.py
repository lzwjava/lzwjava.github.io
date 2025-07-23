import os
import subprocess

from create_note_from_clipboard import create_note

def gpa():
    # Determine the shell command based on the operating system
    if os.name != "nt":
        # For Linux/macOS, use zsh with login shell to load environment variables
        shell_command = "zsh -l -c 'python ~/bin/gitmessageai.py --api deepseek --allow-pull-push'"
    else:
        # For Windows, use cmd.exe to run the Python script
        shell_command = "cmd.exe /c python %USERPROFILE%\\bin\\gitmessageai.py --api deepseek --allow-pull-push'"
    
    # Execute the shell command
    subprocess.run(shell_command, shell=True)

if __name__ == "__main__":
    create_note()
    # Call gpa function
    gpa()
