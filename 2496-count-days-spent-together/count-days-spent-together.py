class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        months = [0, 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
        
        arrive_A = months[int(arriveAlice[:2])] + int(arriveAlice[3:])
        leave_A  = months[int(leaveAlice[:2])] + int(leaveAlice[3:])
        
        arrive_B = months[int(arriveBob[:2])] + int(arriveBob[3:])
        leave_B  = months[int(leaveBob[:2])] + int(leaveBob[3:])
        
        start = max(arrive_A, arrive_B)
        end = min(leave_A, leave_B)
        
        return max(0, end - start + 1)