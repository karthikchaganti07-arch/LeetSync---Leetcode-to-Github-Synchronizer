class Solution:
    def decrypt(self, code: list[int], k: int) -> list[int]:
        n = len(code)
        extend = code + code + code 
        l = []
        for i in range(n):
            if k > 0:
                l.append(sum(extend[n + i + 1 : n + i + 1 + k]))
            elif k < 0:
                l.append(sum(extend[n + i + k : n + i]))
            else:
                l.append(0)
        return l