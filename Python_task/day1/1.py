# # 1. Display numbers from -10 to -1 using for loop
# for i in range(-10,-1+1):
#     print(i,end=" ")
# print("\n")
# # Write a program to display a message “Done” after the successful execution of a for loop that iterates from 0 to 4.
# for i in range(5):
#     print(end="")
# print("Done")


# # Create a program that takes an integer and prints its multiplication table from 1 to 10.
# n=int(input("Enter the number:"))
# for i in range(1,11):
#     print(n,"x",i,"=",(n*i))


# # Write a program that takes an integer n and prints the cube of every number from 1 to n in the format Current Number is : 1 and the cube is 1
# n=int(input("Enter the number:"))
# for i in range(1,n+1):
#     print("Current Number is :",i,"and the cube is ",(i*i*i))


# # Given a Python list, use a loop to print only the elements that are located at odd index positions (index 1, 3, 5, etc.).
# num=["apple",1,"banana",3,"namgo",5,"lemon"]
# for i in range(1,len(num),2):
#     print(num[i],end=" ")


# # Write a program that takes an integer input N and prints its multiplication table from 1 to 10 using a for loop. 

# n=int(input("Enter the number:"))
# for i in range(1,10):
#     print(n,"x",i,"=",(n*i))


# # Write a program to calculate and print the sum of all natural numbers from 1 to a given number N. 
# n=int(input("Enter the number:"))
# sum=0
# for i in range(1,n+1):
#     sum+=i
# print(sum)


# Write a program that prints numbers from 1 to 50. For multiples of 3, print "Fizz" instead of the number. For multiples of 5, print "Buzz". 
# For numbers that are multiples of both 3 and 5, print "FizzBuzz"

# n=int(input("Enter the number:"))
# for i in range(1,50+1):
#     if i%3==0:
#         print("Fizz")
#     elif i%5==0:
#         print("Buzz")
#     elif i%5==0 and i%3==0:
#         print("FizzBuzz")
#     else:
#         print(i)

# Given a list, iterate it in reverse order and print each element.
num=["apple",1,"banana",3,"namgo",5,"lemon"]
for i in range(len(num)-1,-1,-1):
    print(num[i],end=" ")
