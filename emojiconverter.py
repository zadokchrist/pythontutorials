emojidict={
    ':)':"😁",
    ":(":"😒"
}
userinput = input('> ').split(' ')
output=''
for word in userinput:
    output+=emojidict.get(word,word)

print(output)