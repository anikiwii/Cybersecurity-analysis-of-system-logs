import re
from collections import defaultdict
from datetime import datetime

def read_logs(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def filter_events(logs):
    return [line for line in logs if 'Login failed' in line or 'Access denied' in line]

def time_analysis(events):
    activity_patterns = defaultdict(int)

    for event in events:
        hour = re.search(r'\[(.*?)\]', event).group(1)
        activity_patterns[datetime.strptime(hour, '%Y-%m-%d %H:%M:%S').hour] += 1

    return activity_patterns

def generate_report(events, activity_patterns):
    print("=== Cybersecurity Report ===")
    print("Found events:")
    print('\n'.join(f"- {event}" for event in events))

    print("\nTime-based activity analysis:")
    print('\n'.join(f"- Hour {hour}: {count} events" for hour, count in activity_patterns.items()))


# Example usage
file_path = 'path/to/log/file.txt'
logs = read_logs(file_path)
events = filter_events(logs)
activity_patterns = time_analysis(events)
generate_report(events, activity_patterns)
