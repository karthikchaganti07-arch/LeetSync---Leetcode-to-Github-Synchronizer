from collections import Counter
class Solution:
    def similarPairs(self, words: List[str]) -> int:
        counts = Counter()
        pairs = 0
        for word in words:
            char_set = frozenset(word)
            pairs += counts[char_set]
            counts[char_set] += 1
        return pairs