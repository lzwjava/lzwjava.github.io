# screenshot_full_pillow.py
import datetime
from PIL import ImageGrab

ts = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
path = f"screenshot-{ts}.png"

# On macOS, this grabs the full virtual desktop by default.
# If you're on multiple monitors and want everything, try all_screens=True (Pillow ≥10.1).
try:
    img = ImageGrab.grab(all_screens=True)   # falls back to full desktop if unsupported
except TypeError:
    img = ImageGrab.grab()                   # for older Pillow versions

img.save(path)
print(f"Saved {path}  size={img.size}")
