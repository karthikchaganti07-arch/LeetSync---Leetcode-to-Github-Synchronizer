class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        res=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==min(matrix[i]):
                    boolean=True
                    for k in range(len(matrix)):
                        if matrix[k][j] >matrix[i][j]:
                            boolean=False
                            break
                    if boolean:
                        res.append(matrix[i][j])
        return res