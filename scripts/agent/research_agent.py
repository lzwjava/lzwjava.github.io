import os
import sys
import json
import argparse
import datetime
import pyperclip
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from scripts.llm.openrouter_client import call_openrouter_api

def sanitize_filename(filename):
    """Sanitize filename for filesystem compatibility"""
    return "".join(c for c in filename if c.isalnum() or c in (' ', '-', '_')).rstrip()

def research_with_model(query, model, previous_research=None):
    """Research a topic using a specific AI model"""
    
    prompt = f"""You are a research assistant. Provide a comprehensive, well-structured research response for the following topic.

Topic: {query}

Previous research context: {previous_research if previous_research else "None"}

Please provide:
1. Executive summary (2-3 sentences)
2. Key findings and insights
3. Detailed analysis
4. Sources and references (if applicable)
5. Recommendations or next steps

Be thorough but concise. Focus on accuracy and usefulness."""

    try:
        response = call_openrouter_api(prompt, model=model)
        return response
    except Exception as e:
        return f"Error researching with {model}: {str(e)}"

def conduct_multi_model_research(topic, models=None):
    """Conduct research using multiple AI models"""
    
    if models is None:
        models = [
            "anthropic/claude-3.5-sonnet",
            "openai/gpt-4o",
            "google/gemini-flash-1.5",
            "kimi/k1",
            "deepseek/deepseek-chat"
        ]
    
    research_results = {}
    combined_research = ""
    
    print(f"Researching topic: {topic}")
    print(f"Using {len(models)} AI models")
    
    for i, model in enumerate(models, 1):
        print(f"[{i}/{len(models)}] Researching with {model}...")
        
        # Use previous research as context for subsequent models
        result = research_with_model(topic, model, combined_research if i > 1 else None)
        research_results[model] = result
        
        if i == 1:
            combined_research = result
        else:
            # Build cumulative research for context
            combined_research += f"\n\n--- Additional perspective from {model} ---\n{result}"
    
    return research_results

def save_research_results(topic, results):
    """Save research results to the research directory"""
    
    # Create research directory if it doesn't exist
    research_dir = os.path.join(os.path.dirname(__file__), "..", "..", "research")
    os.makedirs(research_dir, exist_ok=True)
    
    # Generate filename with timestamp
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_topic = sanitize_filename(topic[:50])  # Limit filename length
    filename = f"{safe_topic}_{timestamp}.json"
    filepath = os.path.join(research_dir, filename)
    
    # Prepare data structure
    research_data = {
        "topic": topic,
        "timestamp": datetime.datetime.now().isoformat(),
        "models_used": list(results.keys()),
        "results": results,
        "summary": {
            "total_models": len(results),
            "successful_models": len([r for r in results.values() if not str(r).startswith("Error")])
        }
    }
    
    # Save to JSON file
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(research_data, f, indent=2, ensure_ascii=False)
    
    # Also save a readable text version
    text_filename = f"{safe_topic}_{timestamp}.txt"
    text_filepath = os.path.join(research_dir, text_filename)
    
    with open(text_filepath, 'w', encoding='utf-8') as f:
        f.write(f"Research Report: {topic}\n")
        f.write(f"Generated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("=" * 60 + "\n\n")
        
        for model, result in results.items():
            f.write(f"\n--- {model} ---\n")
            f.write(f"{result}\n")
            f.write("-" * 40 + "\n")
    
    return filepath, text_filepath

def main():
    parser = argparse.ArgumentParser(description='Research a topic using multiple AI models')
    parser.add_argument('topic', type=str, nargs='?', help='The topic to research')
    parser.add_argument('--clipboard', '-c', action='store_true', help='Read topic from clipboard')
    parser.add_argument('--models', '-m', type=str, help='Comma-separated list of models to use')
    parser.add_argument('--output-dir', '-o', type=str, help='Custom output directory (default: research/)')
    
    args = parser.parse_args()
    
    # Get topic
    if args.clipboard:
        topic = pyperclip.paste()
    else:
        topic = args.topic if args.topic else input("Enter research topic: ")
    
    if not topic.strip():
        print("Error: No topic provided")
        return
    
    # Parse models if provided
    models = None
    if args.models:
        models = [m.strip() for m in args.models.split(',')]
    
    # Conduct research
    results = conduct_multi_model_research(topic, models)
    
    # Save results
    json_path, txt_path = save_research_results(topic, results)
    
    # Display summary
    print("Research completed!")
    print(f"JSON results saved to: {json_path}")
    print(f"Text report saved to: {txt_path}")
    
    # Show summary of results
    successful = len([r for r in results.values() if not str(r).startswith("Error")])
    print(f"Successfully gathered insights from {successful}/{len(results)} models")
    
    # Copy topic to clipboard for convenience
    pyperclip.copy(topic)
    print("Topic copied to clipboard")

if __name__ == "__main__":
    main()