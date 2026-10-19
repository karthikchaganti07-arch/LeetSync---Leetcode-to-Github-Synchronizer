class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: list[str]) -> str:
        r=""
        for i in licensePlate:
            if i.isalpha():
                r+=i.lower()
        shortest_word=""
        for i in words:
            word_copy = list(i)
            is_valid = True
            for j in r:
                if j not in word_copy:
                    is_valid = False
                    break
                else:
                    word_copy.remove(j)
            if is_valid:
                if shortest_word == "" or len(i) < len(shortest_word):
                    shortest_word = i
        return shortest_word