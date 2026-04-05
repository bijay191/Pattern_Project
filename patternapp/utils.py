import re

def generate_regex(filename):
    # Replace numbers with [0-9]+
    pattern = re.sub(r'\d+', r'[0-9]+', filename)

    # Escape dots
    pattern = pattern.replace('.', r'\.')

    return pattern