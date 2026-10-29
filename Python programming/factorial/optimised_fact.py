# def optfact(n):
#     temp=n
#     # if n<0:
#     #     n*=-1
#     i=1 #least of any number is 1
#     while i*i <=n:
#         if n%i==0:
#             print(i,end=" ")
#         if i != (n//i):
#             print(n//i,end=" ")
#         i+=1

# num=int(input("Enter the number:"))
# if num>0:
#     optfact(num)
# else:
#     print("enter the positive number")


# Count the factors
def countfactor(n):
    i = 1
    count,countcyle = 0,0
    while i * i <= n:
        countcyle+=1
        if n % i == 0:
            count += 1

            if i != n // i:
                count += 1
        i += 1
    return count,countcyle


# Print the factors
def optfact(n):
    i = 1

    while i * i <= n:

        if n % i == 0:
            print(i, end=" ")
            if i != n // i:
                print(n // i, end=" ")
        i += 1

num = int(input("Enter the number: "))

if num > 0:
    res,countcyle= countfactor(num)
    print("The count of factors:", res)
    print("The count of cycle taken for ",num,"is:" ,countcyle)
    print("The factors are:")
    optfact(num)

else:
    print("Enter a positive number")