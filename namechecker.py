name = input("Enter Name : ")

number_characters = len(name)
if number_characters<3:
    print("Name must be atleast 3 characters")
elif number_characters>50:
    print("Name can be maximum 50 characters")
else:
    print("name looks good")