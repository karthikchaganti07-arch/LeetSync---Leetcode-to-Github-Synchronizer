from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        l=defaultdict(list)
        for i in strs:
            k="".join(sorted(i))
            l[k].append(i)
        return list(l.values())