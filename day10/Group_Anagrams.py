from collections import defaultdict
class group:
    def anagrams(self,strs)->list:
        res=defaultdict(list)
        for s in strs:
            count=[0]*26
            for c in s:
                count[ord(c)-ord("a")] +=1
            res[tuple(count)].append(s)
        return list(res.values())
    
strs=["eat", "tea", "tan", "ate", "nat", "bat"]
print(group().anagrams(strs))
