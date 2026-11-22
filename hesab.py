name = input("enter your name :")
print(f"-----welcome your {name}-----")
myhesab = 1000000
while (True) :
    print("1. View Balance")
    print("2. Interpretation")
    print("3. Deposit of Funds")
    print("4. Exit")
    number = int(input("enter your number:"))
    if number == 1 :
        print(f"mojodi hesab to barabar ast ba {myhesab}")
    elif number == 2 :
        number2 = int(input("enter your mablagh:"))
        myhesab = myhesab - number2 
        print(f"amalyiat anjam shod bray didan mojodi adad 1 ra vared konid.")
    elif number == 3 :
        number3 = int(input("enter your mablagh:"))
        myhesab = myhesab + number3
        print(f"amalyiat anjam shod bray didan mojodi adad 1 ra vared konid.")
    elif number == 4 :
        break