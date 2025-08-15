def palindrome(s):
    
    return str(s)==str(s)[::-1]
num=input("enter any number or string:")
if palindrome(num):
    print("number or string is palindrome")
else :
    print("number or string id not palindrome")
