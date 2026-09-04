from collections import Counter
import re
from typing import List

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        ban = set(banned)
        paragraph = paragraph.lower()
        s = re.sub(r'[^a-z]', ' ', paragraph)
        words = s.split()
        words = [word for word in words if word not in ban]
        c = Counter(words)
        return c.most_common(1)[0][0]