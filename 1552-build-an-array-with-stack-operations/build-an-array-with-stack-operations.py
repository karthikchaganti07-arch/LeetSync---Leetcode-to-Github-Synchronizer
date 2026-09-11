class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        l=[]
        for i in range(1,n+1):
            l.append("Push")
            if i not in target:
                l.append("Pop")
            else:
                target.remove(i)
            if len(target)==0:
                break
        return l