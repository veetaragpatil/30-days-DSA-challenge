class duplicate:
    def __init__(self,nums):
        self.nums=nums
    def get_data(self):
        seen=set()
        duplicates=[]
        for num in self.nums:
            if num in seen:
                duplicates.append(num)
            else:
                seen.add(num)
        return list(set(duplicates))
e1=duplicate([1,2,1,3,4,3,5])
print(e1.get_data())
