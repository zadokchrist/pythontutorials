worddictionary = {
    '0':'Zero',
    "1":'One',
    '2':'Two',
    '3':'Three',
    '4':'Four',
    '5':'Five',
    '6':'Six',
    '7':'Seven',
    '8':'Eight',
    '9':'Nine'
}

numbers =input('Enter Phone Number : ')
numbers_in_words=''
for number in numbers:
    numbers_in_words+=worddictionary.get(number,'!')+' '
print(numbers_in_words)