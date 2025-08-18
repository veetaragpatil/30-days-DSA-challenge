from typing import List
class merge:
    def mergearray (self,num1: List[int],m: int, num2: List[int], n: int):
        last=m+n-1
        while m>0 and n>0:
            if num1[m-1]>num2[n-1]:
                num1[last]=num1[m-1]
                m-=1
            else :
                num1[last]=num2[n-1]
                n-=1
            last-=1
        while n>0:
            num1[last]=num2[n-1]
            n-=1
            last-=1
num1 = [1,2,3,0,0,0]
m = 3
num2 = [2,5,6]
n = 3

e1 = merge()
e1.mergearray(num1, m, num2, n)
print(num1)
