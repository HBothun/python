def Ccencrypt():
    text = input('ENTER MESSAGE: ')
    s = int(input('ENTER SHIFT: '))
    result = ''
    for i in range(len(text)):
        char = text[i]
        if (char == ' '):
            result += ' '
        elif (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
        else:
            result += chr((ord(char) + s-97) % 26 + 97)
    print(result)

def texttonum():
    text = str(input('ENTER MESSAGE: '))
    case = text.lower()
    numbers = []
    for i in range(len(case)):
        letter = case[i]
        if letter == ' ':
            numbers += str(chr(32))
        else:
            number = int(ord(letter) - 97)
            numbers.append(number)
    print(numbers)

def Cctexttonum():
    text = str(input('ENTER MESSAGE: '))
    x = int((int(input('ENTER SHIFT: ')) * -1) + 97)
    case = text.lower()
    numbers = []

    for letter in case:
        if letter == ' ':
            numbers.append(' ')
        else:
            number = int(ord(letter) - x)
            if number > 25:
                number = (number - 26)
            numbers.append(number)
    print(numbers)

dec = input('Pick Your Cipher \n\
[Cc] for Ceaser Cipher, \n\
[TN] for Text to Number Cipher, \n\
[CTN] for Text to Number + Ceaser Cipher: \n')

if dec == 'Cc':
    Ccencrypt()
elif dec == 'TN':
    texttonum()
elif dec == 'CTN':
    Cctexttonum()