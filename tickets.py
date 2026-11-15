age = int(input("enter your age:"))
if age < 5:
    print("ticket is free for you.")
elif age >= 5 and age < 18:
    print("ticket is 50000 for you.")
elif age >= 18 and age < 60:
    print("ticket is 100000 for you.")
else:
    print("ticket is 70000 for you.")