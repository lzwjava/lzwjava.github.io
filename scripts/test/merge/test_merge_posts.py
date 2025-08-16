import unittest
import os
import sys
import tempfile
import shutil
from pathlib import Path

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from scripts.merge.merge_posts import combine_posts, get_post_date

class TestCombinePosts(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        
    def tearDown(self):
        shutil.rmtree(self.test_dir)
        
    def create_post(self, filename, title, date, content):
        post_content = f"""---
title: {title}
date: {date}
---
{content}"""
        path = os.path.join(self.test_dir, filename)
        with open(path, "w", encoding="utf-8") as f:
            f.write(post_content)
        return path
        
    def test_get_post_date(self):
        content = """---
title: Test Post
date: 2024-01-01
---
Test content"""
        self.assertEqual(get_post_date(content), "2024-01-01")
        
        # Test with no front matter
        self.assertIsNone(get_post_date("Just content"))
        
        # Test with no date
        content = """---
title: Test Post
---
Content"""
        self.assertIsNone(get_post_date(content))
        
    def test_combine_posts_basic(self):
        # Create test posts
        main_post = self.create_post("main.md", "Main Post", "2024-03-01", "Main content")
        sub_post1 = self.create_post("sub1.md", "Sub Post 1", "2024-02-01", "Sub content 1")
        sub_post2 = self.create_post("sub2.md", "Sub Post 2", "2024-01-01", "Sub content 2")
        
        # Combine posts
        combine_posts([main_post, sub_post1, sub_post2])
        
        # Check if sub posts were deleted
        self.assertFalse(os.path.exists(sub_post1))
        self.assertFalse(os.path.exists(sub_post2))
        
        # Check combined content
        with open(main_post, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Main post should be first (it has the latest date)
        self.assertTrue(content.startswith("---\ntitle: Main Post"))
        
        # Check if sub posts are properly formatted with titles and dates
        self.assertIn("## Sub Post 1, 2024-02-01", content)
        self.assertIn("## Sub Post 2, 2024-01-01", content)
        
    def test_combine_posts_validation(self):
        # Test with single post
        post = self.create_post("single.md", "Single Post", "2024-01-01", "Content")
        combine_posts([post])
        self.assertTrue(os.path.exists(post))  # Should not process single post
        
        # Test with too many posts
        posts = [self.create_post(f"post{i}.md", f"Post {i}", "2024-01-01", "Content") 
                for i in range(11)]
        combine_posts(posts)
        # All posts should still exist as the operation should fail
        for post in posts:
            self.assertTrue(os.path.exists(post))
            
    def test_combine_posts_no_frontmatter(self):
        # Create posts with and without front matter
        main_post = self.create_post("main.md", "Main Post", "2024-03-01", "Main content")
        
        # Create post without front matter
        no_front_post = os.path.join(self.test_dir, "no_front.md")
        with open(no_front_post, "w", encoding="utf-8") as f:
            f.write("Just content without front matter")
            
        combine_posts([main_post, no_front_post])
        
        # Check if no_front_post was deleted
        self.assertFalse(os.path.exists(no_front_post))
        
        # Check if content was properly combined
        with open(main_post, "r", encoding="utf-8") as f:
            content = f.read()
            self.assertIn("Just content without front matter", content)

if __name__ == '__main__':
    unittest.main()