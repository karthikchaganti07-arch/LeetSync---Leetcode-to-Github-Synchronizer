class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        map = {' ': ' '}
        curr = ord('a')
        for char in key:
            if char not in map:
                map[char] = chr(curr)
                curr+= 1
        decode = [map[char] for char in message]
        return "".join(decode)