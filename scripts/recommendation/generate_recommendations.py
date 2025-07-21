import os
import frontmatter
import sys
from datetime import datetime, timedelta
import argparse

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from translation.deepseek_client import call_deepseek_api
from post_utils import get_recent_posts, extract_post_data


def build_prompt(post_data, years, recommend_desc):
    """Build the AI prompt with post data and recommendation criteria."""
    all_posts_with_links = [f"- [{item['title']}](./{item['link']})" for item in post_data]
    return f"""Here is a list of my blog post titles with their links from the last {years} year(s):
{'\n'.join(all_posts_with_links)}

Recommend the ones that would be most interesting to a visitor who is a {recommend_desc}. Focus on technical, programming, or engineering-related topics that align with their interests. Provide a list of recommended titles, each with a brief reason why it's suitable. Format the output as markdown, with recommended titles as bullet points. Include a link to each post in the format [title](./link), where 'link' is the base name of the file. For example, for a post titled 'Car Lamp' with a file name like '2025-07-21-car-lamp-en.md', the link should be './car-lamp-en'. Use the following format for each recommendation:
- [Title](./link): Reason.
"""



def generate_recommendations(output_file=None, years=1, recommend_desc="10-year experienced backend engineer"):
    """Generate AI-based blog post recommendations for a target audience."""
    recent_posts = get_recent_posts(years=years)
    post_data = extract_post_data(recent_posts)
    prompt = build_prompt(post_data, years, recommend_desc)
    ai_response = call_deepseek_api(prompt=prompt)
    final_output_file = determine_output_filename(output_file, recommend_desc)
    write_recommendations_file(final_output_file, ai_response, years, recommend_desc)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate blog post recommendations for backend engineers.")
    parser.add_argument('--file', type=str, default=None, help="Output markdown file name (e.g., '2025-07-22-recommend-for-engineers-en.md'). If not provided, uses today's date and a generated name.")
    parser.add_argument('--years', type=int, default=1, help="Number of years to consider for recent posts.")
    parser.add_argument('--recommend-desc', type=str, default="10-year experienced backend engineer", help="Description of the target audience for recommendations (e.g., '10-year experienced backend engineer').")
    args = parser.parse_args()
    
    generate_recommendations(output_file=args.file, years=args.years, recommend_desc=args.recommend_desc)
