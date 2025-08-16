import os
import sys
import glob
import argparse

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


def get_post_date(content):
    """Extract date from post front matter."""
    parts = content.split("---", 2)
    if len(parts) >= 3:
        front_matter = parts[1]
        for line in front_matter.split('\n'):
            if line.startswith('date:'):
                return line.split(':', 1)[1].strip().strip('"\'')
    return None

def combine_posts(posts):
    """Combine multiple posts: append sub-posts content to main post and delete sub-post files."""
    if len(posts) < 2:
        print("Error: At least 2 posts are required")
        return
    if len(posts) > 10:
        print("Error: Maximum 10 posts allowed")
        return

    # Convert relative paths to absolute paths and read contents
    post_data = []
    for path in posts:
        abs_path = os.path.abspath(path) if not os.path.isabs(path) else path
        if not os.path.exists(abs_path):
            print(f"Error: Post file not found: {abs_path}")
            return
        
        try:
            with open(abs_path, "r", encoding="utf-8") as f:
                content = f.read()
                post_data.append({
                    'path': abs_path,
                    'content': content,
                    'date': get_post_date(content)
                })
        except Exception as e:
            print(f"Error reading file {abs_path}: {e}")
            return

    # Sort posts by date in descending order
    post_data.sort(key=lambda x: x['date'] if x['date'] else '', reverse=True)

    # First post is main post
    main_content = post_data[0]['content']
    main_path = post_data[0]['path']
    print(f"Main post: {main_path}")

    # Process sub posts
    combined_content = main_content
    
    for post in post_data[1:]:
        print(f"Processing sub post: {post['path']}")
        sub_parts = post['content'].split("---", 2)
        
        if len(sub_parts) >= 3:
            front_matter = sub_parts[1]
            sub_body = sub_parts[2].strip()
            
            # Try to extract title and date from front matter
            title = None
            date = None
            for line in front_matter.split('\n'):
                if line.startswith('title:'):
                    title = line.split(':', 1)[1].strip().strip('"\'')
                elif line.startswith('date:'):
                    date = line.split(':', 1)[1].strip().strip('"\'')
            
            # Add title and date as header if found
            if title:
                header = f"## {title}"
                if date:
                    header += f", {date}"
                sub_body = f"{header}\n\n{sub_body}"
        else:
            # No front matter found, use entire content
            sub_body = post['content'].strip()

        if sub_body:
            combined_content += "\n\n---\n\n" + sub_body
        else:
            print(f"Warning: Sub-post has no content to append: {post['path']}")

    # Write combined content back to main post
    try:
        with open(main_path, "w", encoding="utf-8") as f:
            f.write(combined_content)
        print(f"Successfully combined content into: {main_path}")
    except Exception as e:
        print(f"Error writing combined content: {e}")
        return

    print("Combine operation completed successfully!")


if __name__ == "__main__":
    """Main entry point to handle command-line arguments."""
    parser = argparse.ArgumentParser(description="Combine multiple blog posts (max 10)")
    parser.add_argument("posts", nargs="+", help="Paths to post files. First will be main post after sorting by date.")

    args = parser.parse_args()
    combine_posts(args.posts)
