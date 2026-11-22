number = int(input("Enter your pozitive number :"))
zarb = 1
if number > 0 :
    for i in range(1,number+1) :
        zarb *= i
    print(f"your factorial is {zarb}")
else :
    print("to adad manfi vared kardi")