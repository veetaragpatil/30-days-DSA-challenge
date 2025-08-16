def missing_number(arr):
    n=len(arr)
    for i in range(0,n+1):
        if i not in (arr):
            print("the missing number is:",i)
missing_number(arr=[1,2,3,4,5,7,8,9])
