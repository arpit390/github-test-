#program to check the string is palindrome
s = 'mada'
s1 = s[::-1]
print(s1)
if s1==s:
    print("palendrome")
else:
    print("no palendrome")
#to check number is palendrome or not 
num = int(input("enter the value:"))
temp = num
rev = 0
while(num > 0):
    dig = num % 10
    rev = rev * 10 + dig
    num = num // 10
if (temp == rev):
    print(" palendrome")
else:
    print("not palendrome")
    #################################################################################################
# functions in python


 
