from email import message


weight = input("Weight : ")
unit= input("(L)bs or (K)g : ")

if unit.lower() == "l":
    conversion = float(weight)*0.45
    message = f'You are {conversion} kilos'
    print(message)
else:
    conversion=float(weight)/0.45
    print(f'You are {conversion}' +'pounds')
