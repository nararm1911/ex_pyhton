def isPalindrome(s):
    return s == s[::-1]

s = input("please insert text = ")
x = isPalindrome(s)

if x:
    print("Yes")
else:
    print("No")