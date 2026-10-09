class Solution:
    def numberOfPairs(self, nums: list[int]) -> list[int]:
        freq={}
        count=0
        for i in nums:
            freq[i]=freq.get(i,0)+1
        for i in freq:
            count+=freq[i]//2
            freq[i]%=2
        return [count,sum(freq.values())]