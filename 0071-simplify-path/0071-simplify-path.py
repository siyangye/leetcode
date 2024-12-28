class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        substring = path.split("/")
        
        for repo in substring:
            print(repo)
            if repo == "..":
                if stack:
                    stack.pop()
                continue
            if repo == '.':
                continue
            elif repo != "":
                stack.append(repo)
            
        return "/"+"/".join(stack)