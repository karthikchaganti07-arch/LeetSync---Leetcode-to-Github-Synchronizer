class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        c=0
        s=sum(apple)
        sum_c=0
        capacity.sort(reverse = True)
        for i in capacity:
            if sum_c<s:
                c+=1
            sum_c+=i
        return c