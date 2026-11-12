def login_required(greet):
    print("Details procesing.....")
    flag=False
    def secverification():
        flag=True
        print("Second verification....")
        ref=greet(flag)

    return secverification
@login_required
def greet(flag):
    if flag:
        print("User login")
    else:
        print("User not login")
greet()