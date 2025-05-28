import os
import subprocess
from pathlib import Path

# Configuration
TARGET_DIRS = ["notes", "original"]  # Directories to process
FIX_SCRIPT = "scripts/content/fix_mathjax.py"
PYTHON_CMD = "python3"  # or "python" if that's what works on your system

def process_md_files(directory):
    """Process all .md files in the given directory"""
    dir_path = Path(directory)
    md_files = list(dir_path.glob("*.md"))
    
    if not md_files:
        print(f"⚠️ No .md files found in {directory}/")
        return 0, 0
    
    print(f"\n📂 Processing {len(md_files)} files in {directory}/")
    success_count = 0
    fail_count = 0

    for md_file in md_files:
        file_path = md_file.resolve()
        command = [
            PYTHON_CMD,
            FIX_SCRIPT,
            "--file",
            str(file_path),
            "--reset"
        ]

        print(f"\n🔧 Processing: {file_path}")
        try:
            result = subprocess.run(
                command,
                check=True,
                capture_output=True,
                text=True,
                env=os.environ  # Pass through environment variables (for proxy)
            )
            print(result.stdout.strip())  # Show proxy detection message
            print(f"✅ Success")
            success_count += 1
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed:")
            print(e.stderr.strip())
            print(f"Command: {' '.join(command)}")
            fail_count += 1
    
    return success_count, fail_count

def main():
    total_success = 0
    total_fail = 0

    for directory in TARGET_DIRS:
        if not Path(directory).exists():
            print(f"⚠️ Directory not found: {directory}/")
            continue
        
        success, fail = process_md_files(directory)
        total_success += success
        total_fail += fail

    print("\n📊 Final Results:")
    print(f"  Total files processed: {total_success + total_fail}")
    print(f"  Successful: {total_success}")
    print(f"  Failed:     {total_fail}")

    if total_fail > 0:
        print("\n💡 For failed files, try running manually with:")
        print(f"   {PYTHON_CMD} {FIX_SCRIPT} --file PATH/TO/FILE.md --reset")

if __name__ == "__main__":
    main()