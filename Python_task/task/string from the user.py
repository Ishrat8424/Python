# 4.Write a Python program that accepts a string from the user and displays: 
str=input("Enter the string:")
print("\nLength of the string is:",len(str))
print("\nFirst character:",str[0])
print("\nLast character:",str[len(str)-1])
print("\nuppercase:",str.upper())
print("\nlowercase:",str.lower())
count=0
for i in str:
    if i=='a' or i=='A':
        count+=1

print("\nNumber of occurrences of 'a':",count)
print("\nReversed string:",str[::-1])