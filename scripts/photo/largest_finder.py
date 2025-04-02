import os
from pathlib import Path

def find_largest_videos(directory, top_n=20):
    video_extensions = {'.mp4', '.mov', '.avi', '.mkv', '.flv', '.wmv', '.m4v'}
    video_files = []
    
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = Path(root) / file
            if file_path.suffix.lower() in video_extensions:
                video_files.append((file_path, file_path.stat().st_size))
    
    video_files.sort(key=lambda x: x[1], reverse=True)
    
    for i, (path, size) in enumerate(video_files[:top_n], 1):
        print(f"{i}. {path} - {size / (1024 * 1024):.2f} MB")

if __name__ == "__main__":
    photos_library_path = "/Users/lzwjava/Pictures/Photos Library.photoslibrary/"
    find_largest_videos(photos_library_path)
