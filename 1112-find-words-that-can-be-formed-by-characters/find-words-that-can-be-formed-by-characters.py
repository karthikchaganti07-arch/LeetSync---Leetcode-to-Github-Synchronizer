class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count=0
        for word in words:
            temp=chars
            valid=True
            for j in word:
                if j in temp:
                    temp=temp.replace(j,"",1)
                else:
                    valid=False
                    break
            if valid:
                count+=len(word)
        return count