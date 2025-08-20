class subzero:
    def subarray(self,arr):
        prefix_sum=0
        sum_map={}
        result=[]
        for i,num in enumerate(arr):
            prefix_sum+=num
            if prefix_sum==0:
                result.append((0,i))
            if prefix_sum in sum_map:
                for start_index in sum_map[prefix_sum]:
                    result.append((start_index +1,i))
            sum_map.setdefault(prefix_sum,[]).append(i)
        return result
    
arr=[3,4,-7,1,-1]
subzero1=subzero().subarray(arr)
for s,e in subzero1:
    print(arr[s:e+1])
