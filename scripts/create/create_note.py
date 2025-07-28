import os
import subprocess
import platform

from create_note_from_clipboard import create_note

def gpa():
    # Determine the shell command based on the operating system
    system = platform.system()
    if system == "Linux":
        # For Linux, use bash with login shell to load environment variables
        shell_command = "bash -l -c 'python ~/bin/gitmessageai.py --api deepseek --allow-pull-push'"
    elif system == "Darwin":
        # For macOS, use zsh with login shell to load environment variables
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