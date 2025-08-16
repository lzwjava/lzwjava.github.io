import json
import os
import shutil

def sync_config():
    source_path = os.path.expanduser("~/.claude-code-router/config.json")
    target_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "config")
    target_path = os.path.join(target_dir, "claude_code_config.json")
    
    # Read source config
    with open(source_path) as f:
        config = json.load(f)
    
    # Replace sensitive info
    if "Providers" in config:
        for provider in config["Providers"]:
            if "api_key" in provider:
                provider["api_key"] = ""
    
    # Write sanitized config
    with open(target_path, "w") as f:
        json.dump(config, f, indent=2)

if __name__ == "__main__":
    sync_config()