class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        cover= set()
        for start, end in ranges:
            for num in range(start, end + 1):
                cover.add(num)
        for target in range(left, right + 1):
            if target not in cover:
                return False
        return True