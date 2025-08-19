import json
import os

def reverse_sync_config():
    print("Starting reverse config sync...")

    # Source: the sanitized config in your project
    project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    source_path = os.path.join(project_dir, "config", "claude_code_config.json")
    print(f"Source config path: {source_path}")

    # Target: the original config location on macOS
    target_dir = os.path.expanduser("~/.claude-code-router")
    target_path = os.path.join(target_dir, "config.json")
    print(f"Target config path: {target_path}")

    # Check if source exists
    if not os.path.exists(source_path):
        raise FileNotFoundError(f"Source config not found: {source_path}")

    # Create target directory if it doesn't exist
    os.makedirs(target_dir, exist_ok=True)

    # Read the sanitized config
    with open(source_path) as f:
        config = json.load(f)

    # Write config back to original location
    print("Writing config back to original location...")
    with open(target_path, "w") as f:
        json.dump(config, f, indent=2)

    print("Reverse config sync completed successfully")

if __name__ == "__main__":
    reverse_sync_config()
