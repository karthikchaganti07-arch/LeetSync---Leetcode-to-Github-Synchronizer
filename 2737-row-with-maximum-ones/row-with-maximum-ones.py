class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        r=[0,0]
        for row in mat:
            c=row.count(1)
            if r[1]<c:
                r=[mat.index(row),c]
        return r