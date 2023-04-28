from collections import Counter
from typing import Dict


def get_frequencies_of_text(text: str) -> Dict[str, int]:
    return Counter(text)
