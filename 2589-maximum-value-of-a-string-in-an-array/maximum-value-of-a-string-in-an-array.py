class Solution:
    def maximumValue(self, strs: list[str]) -> int:
        max_val = 0
        for i in strs:
            if i.isdigit():
                current_value = int(i)
            else:
                current_value = len(i)
            if current_value > max_val:
                max_val = current_value
        return max_val