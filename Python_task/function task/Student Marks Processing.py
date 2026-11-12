def calavg(marks):
    sum=0
    for i in range(0,len(marks)):
        sum=sum+marks[i]
    return sum//len(marks)
marks = [35, 45, 67, 89, 90, 23, 56, 78, 99] 
print("The average marks:",calavg(marks))
print("--------------------------------------------------------")
result = sorted(marks, key=lambda x: x, reverse=True)
print(result)
print("--------------------------------------------------------")
k=list(filter(lambda x:x>60,marks))
print("Use filter to find marks above 60:",k)
print("--------------------------------------------------------")
grade = list(map(lambda x: 
    'A' if x >= 90 else
    'B' if x >= 80 else
    'C' if x >= 70 else
    'D' if x >= 60 else 'F', marks))

print("Use map to convert marks into grades:",grade)
print("--------------------------------------------------------")
def pass_fail_generator(pass_mark):

    def check(marks):
        if marks >= pass_mark:
            return "Pass"
        else:
            return "Fail"

    return check


check_result = pass_fail_generator(40)
result = list(map(check_result, marks))
print("Pass/Fail:", result)
print("--------------------------------------------------------")

def marks_decorator(fun):

    def inner():
        print("Marks processing started")
        fun()

    return inner

@marks_decorator
def process_marks():
    print("Processing student marks...")


process_marks()