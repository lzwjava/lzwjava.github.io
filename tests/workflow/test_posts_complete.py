import unittest

from scripts.content.find_orphaned_posts import analyze_post_completeness

class TestPostsComplete(unittest.TestCase):
    def test_no_orphaned_posts(self):
        orphaned_posts, _ = analyze_post_completeness()
        self.assertEqual(len(orphaned_posts), 0, f"There are {len(orphaned_posts)} orphaned posts: {[post['base_name'] for post in orphaned_posts]}")

if __name__ == '__main__':
    unittest.main()