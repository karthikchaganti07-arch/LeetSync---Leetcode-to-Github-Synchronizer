class Solution:
    def minQueenMoves(self, source: list[int], target: list[int]) -> int:
        if source == target:
            return 0
        sr, sc = source
        tr, tc = target
        if sr == tr or sc == tc or (sr - sc == tr - tc) or (sr + sc == tr + tc):
            return 1
        return 2