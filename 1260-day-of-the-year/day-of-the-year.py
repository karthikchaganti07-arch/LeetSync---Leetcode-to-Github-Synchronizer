class Solution:
    def dayOfYear(self, date: str) -> int:
        year = int(date[:4])
        month = int(date[5:7])
        day = int(date[8:])
        days = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]
        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            if month > 2:
                return days[month - 1] + day + 1
        return days[month - 1] + day