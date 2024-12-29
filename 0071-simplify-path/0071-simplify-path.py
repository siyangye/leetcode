class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        curr = ""

        for c in path+"/":
            if c == "/":
                if curr == "..":
                    if stack:
                        stack.pop()
                    curr = ""
                elif curr == ".":
                    curr = ""
                elif curr != "":
                    stack.append(curr)
                    curr =""
            else:
                curr+= c
        print(stack)
        return "/" +"/".join(stack)