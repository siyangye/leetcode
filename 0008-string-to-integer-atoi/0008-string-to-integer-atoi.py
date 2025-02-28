class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s) == 0:
            return 0
        i = 0
        while i < len(s) and s[i] ==' ':
            i += 1
        if i == len(s):
            return 0

        sign = 1
        if s[i] == "-":
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1

        res = 0
        while i < len(s) and s[i].isdigit():
            res = res * 10 + int(s[i])
            i += 1
        res *= sign
        
        int_min = -2**31
        int_max = 2**31 - 1
        if res < int_min:
            res = int_min
        elif res > int_max:
            res = int_max
        return res
