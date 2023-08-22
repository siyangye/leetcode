class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #key: sorted words "tea" -> ['a','e','t']
        #value: corresponding word 
        #{key:value, key:value}, return the value 
        #correct: 
        hashMap = {}
        for i in strs:
            #key = sorted(i) #this is a list, you cannot use list as key as it is mutable
            key = ''.join(sorted(i))
            print(key)
            if key in hashMap:
                hashMap[key].append(i)
            else:
                hashMap[key] = [i] 
        anagramList = list(hashMap.values())
        return anagramList 
        
        # #有问题的code:
        #    #key: sorted words "tea" -> ['a','e','t']
        # #value: corresponding word 
        # #{key:value, key:value}, return the value 
        # hashMap = {}
        # for i in strs:
        #     #key = sorted(i) #this is a list, you cannot use list as key as it is mutable
        #     key = ''.join(sorted(i))
        #     print(key)
        #     if key in hashMap:
        #         hashMap[key].append(i)
        #     hashMap[key] = [i] 
        # anagramList = list(hashMap.values())
        # return anagramList 
    