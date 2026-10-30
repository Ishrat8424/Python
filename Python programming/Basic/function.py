def divideNum(num,dec):
    rem=num%dec
    return rem
    print("The remainder is:",divideNum(10,3))


result=divideNum(10,3)
print("The remainder is:",result)


result=divideNum(result,4)
print("The remainder is:",result)