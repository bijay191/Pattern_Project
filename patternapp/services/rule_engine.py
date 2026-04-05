# patternapp/services/rule_engine.py

import re

def generate_rule_pattern(file_list):
    patterns = []

    for file in file_list:
        temp = ""
        for ch in file:
            if ch.isalpha():
                temp += "[a-zA-Z]"
            elif ch.isdigit():
                temp += r"\d"
            else:
                temp += re.escape(ch)
        patterns.append(temp)

    base = patterns[0]

    base = re.sub(r"(\[a-zA-Z\])+", "[a-zA-Z]+", base)
    base = re.sub(r"(\\d)+", r"\\d+", base)

    return base