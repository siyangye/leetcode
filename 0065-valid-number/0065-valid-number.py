class Solution:
    def isNumber(self, s: str) -> bool:
        def is_valid_int(s:str):
            seen_num = False
            if not s:
                return False
            i=0
            if s[i] in ['+','-']:
                i+=1
            while i<len(s):
                if s[i].isdigit():
                    i+=1
                    seen_num = True
                else:
                    return False
            return seen_num

        seen_num = False
        count_dot = 0
        count_e = 0
        i=0
        if s[i] in ['+','-']:
            i+= 1
        while i < len(s):
            if s[i]=='.':
                count_dot += 1
                print(count_dot)
            elif s[i] in ['e','E']:
                count_e +=1
                return count_dot <=1 and seen_num and is_valid_int(s[i+1:])
            elif s[i].isdigit():
                seen_num = True
            else:
                return False
            i+=1
        print(count_dot)
        return count_dot <=1 and count_e <=1 and seen_num