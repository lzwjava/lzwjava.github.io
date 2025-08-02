import subprocess
import sys

def run_vscode_command(prompt: str = "") -> bool:
    """
    Execute a VS Code command using the 'code' CLI.
    
    Args:
        command (str): The VS Code command to execute (e.g., 'workbench.action.chat.open').
        prompt (str): Optional prompt or argument for the command.
    
    Returns:
        bool: True if the command was executed successfully, False otherwise.
    """
    try:
        # Construct the VS Code CLI command
        # Assumes 'code' is in the system PATH
        cmd = ['code', 'chat', prompt]

        # Run the command
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=True
        )
        
        # Print the command output
        print("Command output:", result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Failed to execute command: {e.stderr}", file=sys.stderr)
        return False
    except FileNotFoundError:
        print("VS Code CLI ('code') not found. Ensure VS Code is installed and added to PATH.", file=sys.stderr)
        return False

def main():
    # The extension command to trigger
    # Run the command
    success = run_vscode_command()
    if success:
        print(f"Successfully triggered  with prompt: {prompt}")
    else:
        print(f"Failed to trigger")

if __name__ == "__main__":
    main()