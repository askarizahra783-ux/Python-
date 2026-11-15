salary = int(input("enter your salary:"))
child = input("enter your child (y/n):")
if salary <= 10000000:
    maliat = 0
else:
    if salary > 10000000 and salary <= 25000000:
        maliat = (salary - 10000000) * 0.10
    else:
        maliat = 1500000 + (salary - 25000000) * 0.20
    if child == 'y':
        maliat = maliat - 500000
print(f"salary:{salary}")
print(f"child:{child}")
print(f"maliat nahayi:{maliat}")