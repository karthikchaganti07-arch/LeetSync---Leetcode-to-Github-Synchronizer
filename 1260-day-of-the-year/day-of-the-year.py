class Solution:
    def dayOfYear(self, date: str) -> int:
        year,month,days=map(int,date.split("-"))
        is_leap=(year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)
        feb_days=29 if is_leap else 28
        month_days=[31, feb_days, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return sum(month_days[:month-1])+days