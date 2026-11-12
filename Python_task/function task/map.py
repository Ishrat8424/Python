temp=[0, 25, 30, 37, 100] 
print(temp)
k=list(map(lambda x:((x*9/5)+32),temp))
print("convert Celsius to Fahrenheit:",k)

k=list(map(lambda x:x*x,temp))
print("Convert all numbers into squares:",k)

string=input("Enter the string:")
k1=''.join(map(lambda x:x.upper(),string))
print("Convert all names into uppercase:",k1)

k=list(map(lambda x:x+100,temp))
print("Add 100 to each number in a list:",k)