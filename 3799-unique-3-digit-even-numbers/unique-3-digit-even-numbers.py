from itertools import permutations
class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        unique=set()
        for i in permutations(digits,3):
            if i[0]==0:
                continue
            if i[-1]%2==0:
                unique.add(i)
        return len(unique)