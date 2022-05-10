numbers=[1,3,34,35,3,3,5,6,7,3,3,6]
uniques =[]
for number in numbers:
    if number not in uniques:
        uniques.append(number)

print(uniques)