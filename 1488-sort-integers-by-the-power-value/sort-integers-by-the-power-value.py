class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        l = []
        for i in range(lo, hi + 1):
            original = i
            steps = 0
            while i != 1:
                if i % 2 == 0:
                    i = i // 2
                else:
                    i = 3 * i + 1
                steps += 1
            l.append((steps, original))
        l.sort()
        return l[k - 1][1]