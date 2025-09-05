import sys
import random
from datetime import datetime, timedelta
from gpa import gpa
from create_note_from_clipboard import create_note

def parse_args():
    """Parse command line arguments"""
    use_random_date = False
    if len(sys.argv) > 1 and sys.argv[1] == "--random":
        use_random_date = True
    return use_random_date

def generate_random_date():
    """Generate a random date within the last 180 days"""
    end_date = datetime.now()
    start_date = end_date - timedelta(days=180)
    
    random_days = random.randint(0, 180)
    random_date = start_date + timedelta(days=random_days)
    
    return random_date.strftime('%Y-%m-%d')

if __name__ == "__main__":
    use_random_date = parse_args()
    random_date = generate_random_date() if use_random_date else None
    
    create_note(date=random_date)
    # Call gpa function
    gpa()
