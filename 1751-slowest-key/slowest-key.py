class Solution:
    def slowestKey(self, releaseTimes: list[int], keysPressed: str) -> str:
        r = keysPressed[0]
        m = releaseTimes[0]
        for i in range(1, len(releaseTimes)):
            duration = releaseTimes[i] - releaseTimes[i - 1]
            if m < duration:
                r = keysPressed[i]
                m = duration
            elif m == duration:
                if keysPressed[i] > r:
                    r = keysPressed[i]  
        return r