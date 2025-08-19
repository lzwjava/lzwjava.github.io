import json
import os
import shutil

def reverse_sync_config():
    print("Starting reverse config sync...")

    # Source: the sanitized config in your project
    project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    source_path = os.path.join(project_dir, "config", "claude_code_config.json")
    print(f"Source config path: {source_path}")

    # Target: the original config location on macOS
    target_path = os.path.expanduser("~/.claude-code-router/config.json")
    print(f"Target config path: {target_path}")

    # Read the sanitized config
    with open(source_path) as f:
        config = json.load(f)

    # Here, you may want to prompt the user to manually enter sensitive info,
    # or restore from a backup if needed.
    # For now, just copy as-is (assuming you handle sensitive info separately)
    print("Writing config back to original location...")
    with open(target_path, "w") as f:
        json.dump(config, f, indent=2)

    print("Reverse config sync completed successfully")

if __name__ == "__main__":
    reverse_sync_config()
