import math 

def checkPalindrome(num):
    s = str(num)
    ln = len(s)
    # print(ln,ln//2)
    for i in range(ln//2):
        if s[i] != s[ln-i - 1]:
            return False
    return True
    
        

num = int(input("Enter number: "))
if checkPalindrome(num):
    print(f"{num} is palindrome")
else:
    print(f"{num} is not palindrome")
        