# WAP to reverse all the numbers present in a user defined range and display in decreasing order
def reverseNumber(n):
    temp = n
    if n < 0:
        n = -n
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n = n // 10
    if temp < 0:
        rev = -rev
    return rev
#------------------------------------------------------------------
start = int(input("Enter starting range: "))
end = int(input("Enter ending range: "))

if start > end:
    start, end = end, start

#------largenum-----------
largest = reverseNumber(start)
smallest = largest
for i in range(start, end + 1):
    rev = reverseNumber(i)

    if rev > largest:
        largest = rev

    if rev < smallest:
        smallest = rev
#---------------------------------------------
print("Reversed numbers in decreasing order:")

while largest >= smallest:

    nextLargest = smallest - 1

    for i in range(start, end + 1):
        rev = reverseNumber(i)

        if rev == largest:
            print(rev, end=" ")

        elif rev < largest and rev > nextLargest:
            nextLargest = rev

    largest = nextLargest