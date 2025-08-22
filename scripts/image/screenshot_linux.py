import subprocess
import datetime
import os
from PIL import Image

# Create screenshots directory if it doesn't exist
screenshot_dir = "assets/screenshots"
os.makedirs(screenshot_dir, exist_ok=True)

# Generate filename with format: yearmmdd_hhmm.png
ts = datetime.datetime.now().strftime("%Y%m%d_%H%M")
path = os.path.join(screenshot_dir, f"{ts}.png")

# Method 1: Use scrot (if available)
try:
    subprocess.run(["scrot", path], check=True)
    print(f"Saved screenshot to {path} using scrot")
except (subprocess.CalledProcessError, FileNotFoundError):
    
    # Method 2: Use ImageMagick's import command
    try:
        subprocess.run(["import", "-window", "root", path], check=True)
        print(f"Saved screenshot to {path} using ImageMagick")
    except (subprocess.CalledProcessError, FileNotFoundError):
        
        # Method 3: Use gnome-screenshot (GNOME environments)
        try:
            subprocess.run(["gnome-screenshot", "-f", path], check=True)
            print(f"Saved screenshot to {path} using gnome-screenshot")
        except (subprocess.CalledProcessError, FileNotFoundError):
            
            # Method 4: Use spectacle (KDE environments)
            try:
                subprocess.run(["spectacle", "-b", "-n", "-o", path], check=True)
                print(f"Saved screenshot to {path} using spectacle")
            except (subprocess.CalledProcessError, FileNotFoundError):
                
                # Method 5: Use xwd (X11 fallback)
                try:
                    # Take screenshot with xwd
                    xwd_path = os.path.join(screenshot_dir, f"{ts}.xwd")
                    subprocess.run(["xwd", "-root", "-out", xwd_path], check=True)
                    
                    # Convert xwd to png using ImageMagick
                    subprocess.run(["convert", xwd_path, path], check=True)
                    
                    # Clean up xwd file
                    if os.path.exists(xwd_path):
                        os.remove(xwd_path)
                    
                    print(f"Saved screenshot to {path} using xwd + convert")
                except (subprocess.CalledProcessError, FileNotFoundError):
                    
                    # Method 6: Use ffmpeg (last resort)
                    try:
                        subprocess.run([
                            "ffmpeg", "-f", "x11grab", "-s", "1920x1080", "-i", ":0.0",
                            "-frames:v", "1", path
                        ], check=True, capture_output=True)
                        print(f"Saved screenshot to {path} using ffmpeg")
                    except (subprocess.CalledProcessError, FileNotFoundError):
                        print("No suitable screenshot tool found. Please install one of: scrot, ImageMagick, gnome-screenshot, spectacle, or ffmpeg.")

# If screenshot was taken, show basic info
if os.path.exists(path):
    try:
        with Image.open(path) as img:
            print(f"Screenshot saved successfully: {path}")
            print(f"Image size: {img.size[0]}x{img.size[1]}")
            print(f"Image format: {img.format}")
    except Exception as e:
        print(f"Could not read image info: {e}")