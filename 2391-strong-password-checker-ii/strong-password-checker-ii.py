class Solution:
    def strongPasswordCheckerII(self, p: str) -> bool:
        is_len=is_lower=is_upper=is_digit=is_spl=False
        spl="!@#$%^&*()-+"
        l=""
        for i in range(len(p)):
            l+=p[i]
            if len(l)>=8:
                is_len=True
            if p[i].isdigit():
                is_digit=True
            elif p[i] in spl:
                is_spl=True
            elif p[i].isalpha():
                if p[i].islower():
                    is_lower=True
                else:
                    is_upper=True
            if i > 0 and p[i] == p[i-1]:
                return False
        return True if is_len and is_lower and is_upper and is_digit and is_spl else False