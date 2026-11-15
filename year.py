year = int(input("enter your year of birth:"))
if year % 400 == 0:
    print("ble sale vared shode be kabise ast.")
elif year % 100 == 0:
    print("na sale vared shode be kabise nist.")
elif year % 4 == 0:
    print("ble sale vared shode be kabise ast.")
else:
    print("na sale vared shode be kabise nist.")