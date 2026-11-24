from collections import Counter
class Solution:
    def mergeSimilarItems(self, items1: list[list[int]], items2: list[list[int]]) -> list[list[int]]:
        c=Counter()
        for val,weight in items1+items2:
            c[val]+=weight
        return sorted([[val,weight] for val,weight in c.items()])