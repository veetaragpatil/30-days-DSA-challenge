from collections import defaultdict
def atMostK(s, k):
    count = defaultdict(int)
    left = 0
    res = 0
    distinct = 0    
    for right in range(len(s)):
        if count[s[right]] == 0:
            distinct += 1
        count[s[right]] += 1      
        while distinct > k:
            count[s[left]] -= 1
            if count[s[left]] == 0:
                distinct -= 1
            left += 1        
        res += (right - left + 1) 
    return res
def substringsWithKDistinct(s, k):
    return atMostK(s, k) - atMostK(s, k-1)
s = "pqpqs"
k = 2
print(substringsWithKDistinct(s, k)) 
