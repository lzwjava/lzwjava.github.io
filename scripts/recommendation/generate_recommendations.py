import os
import sys
import argparse
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from deepseek_tool_client import call_deepseek_api
from post_utils import get_recent_posts, extract_post_data
from output_utils import determine_output_filename, write_recommendations_file


def build_prompt(post_titles, years, recommend_desc):
    """Build the AI prompt with post titles and recommendation criteria."""
    all_posts_with_titles = [f"- {title}" for title in post_titles]
    return f"""Here is a list of my blog post titles from the last {years} year(s):
{'\n'.join(all_posts_with_titles)}

Recommend the ones that would be most interesting to a visitor who is a {recommend_desc}. Focus on topics that align with their interests. 

First, select the most suitable titles and prepare brief reasons why each is suitable.

Then, for each selected title, call the 'get_link' tool to retrieve the link for that title. The tool will return a JSON object like {{"link": "example-link"}} or {{"error": "Title not found"}}.

Finally, format the output as markdown, with recommended titles as bullet points. Include a link to each post in the format [title](./link), where 'link' is the base name obtained from the tool. Use the following format for each recommendation:
- [Title](./link): Reason.

If a link cannot be found, skip that recommendation or note it appropriately."""


def generate_recommendations(output_file=None, years=1, recommend_desc="10-year experienced backend engineer"):
    """Generate AI-based blog post recommendations for a target audience using tool calls."""
    recent_posts = get_recent_posts(years=years)
    post_data = extract_post_data(recent_posts)
    
    post_titles = sorted([item['title'] for item in post_data])
    title_to_link = {item['title']: item['link'] for item in post_data}
    
    prompt = build_prompt(post_titles, years, recommend_desc)
    
    # Define the tool for getting links
    tools = [
        {
            "type": "function",
            "function": {
                "name": "get_link",
                "description": "Retrieve the link for a given blog post title. The link is the base name used in the URL.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "title": {
                            "type": "string",
                            "description": "The exact title of the blog post."
                        }
                    },
                    "required": ["title"]
                }
            }
        }
    ]
    
    # System prompt for the AI
    system_prompt = "You are a helpful assistant that recommends blog posts. Use the provided tools to get links for selected titles before formatting the final output."
    
    # Initial messages
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": prompt}
    ]
    
    # Call the API (assuming call_deepseek_api now supports messages and tools, and returns the response message object)
    response_message = call_deepseek_api(messages=messages, tools=tools)
    # Call the API (assuming call_deepseek_api now supports messages and tools, and returns the response message object)
    response_message = call_deepseek_api(messages=messages, tools=tools)
    # Convert SimpleNamespace to dict if needed
    messages.append(vars(response_message) if not isinstance(response_message, dict) else response_message)
    
    # Handle tool calls in a loop
    while hasattr(response_message, 'tool_calls') and response_message.tool_calls:
        for tool_call in response_message.tool_calls:
            function_name = tool_call.function.name
            if function_name == "get_link":
                try:
                    args = json.loads(tool_call.function.arguments)
                    title = args['title']
                    link = title_to_link.get(title)
                    if link:
                        tool_response = json.dumps({"link": link})
                    else:
                        tool_response = json.dumps({"error": "Title not found"})
                except Exception as e:
                    tool_response = json.dumps({"error": f"Error processing tool call: {str(e)}"})
                
                messages.append({
                    "role": "tool",
                    "content": tool_response,
                    "tool_call_id": tool_call.id
                })
        
        # Call the API again with updated messages
        response_message = call_deepseek_api(messages=messages, tools=tools)
        # Convert SimpleNamespace to dict if needed
        messages.append(vars(response_message) if not isinstance(response_message, dict) else response_message)
    ai_response = response_message.content if hasattr(response_message, 'content') else ""
    
    final_output_file = determine_output_filename(output_file, recommend_desc)
    write_recommendations_file(final_output_file, ai_response, years, recommend_desc)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate blog post recommendations for backend engineers.")
    parser.add_argument('--file', type=str, default=None, help="Output markdown file name (e.g., '2025-07-22-recommend-for-engineers-en.md'). If not provided, uses today's date and a generated name.")
    parser.add_argument('--years', type=int, default=1, help="Number of years to consider for recent posts.")
    parser.add_argument('--recommend-desc', type=str, default="10-year experienced backend engineer", help="Description of the target audience for recommendations (e.g., '10-year experienced backend engineer').")
    args = parser.parse_args()
    
    generate_recommendations(output_file=args.file, years=args.years, recommend_desc=args.recommend_desc)