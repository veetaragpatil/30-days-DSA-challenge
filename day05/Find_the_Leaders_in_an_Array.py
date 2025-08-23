from typing import List
class leader:
    def leader_num(self,nums)->[int]:
        LD=[]
        n = len(nums)
        max_from_right = nums[-1]  
        LD.append(max_from_right)

        
        for i in range(n-2, -1, -1):
            if nums[i] >= max_from_right:
                LD.append(nums[i])
                max_from_right = nums[i]

        return LD[::-1]
nums=[16,17,4,3,5,2]

print(leader().leader_num(nums))
