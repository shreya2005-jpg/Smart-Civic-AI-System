
import re

def extract_location(text):
    match = re.search(r"near (.*)|in (.*)", text)

    if match:
        return match.group(1) or match.group(2)

    return "Unknown Location"
