# patternapp/services/regex_generator.py

from .rule_engine import generate_rule_pattern
from .ai_refiner import refine_regex


def generate_regex(file_list):
    rough = generate_rule_pattern(file_list)
    refined = refine_regex(file_list, rough)

    return refined if refined else rough