class Solution:
    def isNumber(self, s: str) -> bool:
        def valid_int(s:str):
            if not s:
                return False
            seen_num = False
            i = 0
            if s[i] in ['+','-']:
                i+=1
            while i <len(s):
                if s[i].isdigit():
                    i+=1
                    seen_num = True
                else:
                    return False
            return seen_num
        seen_dot = False
        seen_num = False
        i = 0
        if s[i] in ['+','-']:
            i+=1
        while i < len(s):
            if s[i].isalpha():
                if s[i] not in ['e','E']:
                    return False
                else:
                    return seen_num and valid_int(s[i+1:])
            elif s[i] in ['+','-']:
                return False
            elif s[i]=='.':
                if not seen_dot:
                    seen_dot = True
                else:
                    return False
            elif s[i].isdigit():
                seen_num = True
            i+=1
        return seen_num