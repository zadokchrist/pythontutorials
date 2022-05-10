def emojiconnverter(input):
    output=''
    emojidict={
    ':)':"😁",
    ":(":"😒"
    }
    for word in input.split(' '):
        output+=emojidict.get(word,word)
    return output


converted_word =emojiconnverter(input('Enter Word : '))
print(converted_word)