number = int(input("Enter your number:"))
jam = 0
for i in range(2,number) :
    if number % i == 0 :
        jam += 1
if jam > 0 :
    print(f"adad {number} adad aval nist.")

else :
    print(f"adad {number} adad aval ast.")
    