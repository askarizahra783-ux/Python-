import random
myname=input("enter youe name:")
print(f"-----welcome your {myname}-----" )
print("Main Menu")
print("1. Password Generator ")
print("2. Number Guessing Game ")
print("3. Exit ")
number = int(input("Enter your number:"))
if number==1 :
    myPassword = ""
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%&!"
    myLength = int(input("Enter your Password Length :"))
    for i in range(myLength) :
        myPassword += random.choice(chars)
    print(f" Password your is {myPassword}")
elif number==2 :
    Snumber = random.randint(1,100)
    for i in range(1,8,1):
        Gnumber=int(input("enter youe secret number:"))
        if Gnumber == Snumber :
            print(f"tabrik migham to barande shody😍👏")
            break;
        elif i < 7 :
            if Gnumber > Snumber :
                print(f"adad vared shode bozorghtar az adad makhfi ast😒 dobare talash kon.")
            else :
                print(f"adad vared shode kochektar az adad makhfi ast😒 dobare talash kon.")
    else :
        print("talash hay to tamam shod to bakhty😐😔")
elif number == 3 :
    print(f"Goodby {myname}🖐")