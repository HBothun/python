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


def scramble():
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


def DCcencrypt():
    x = str(input('ENTER MESSAGE: '))
    letters = 'abcdefghijklmnopqrstuvwxyz'
    caps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for key in range(len(letters)):
        translated = ''
        for i in range(len(x)):
            symbol = x[i]
            if symbol in letters:
                num = letters.find(symbol)
                num = num - key
                if num < 0:
                    num = num + len(letters)
                translated = translated + letters[num]
            elif symbol in caps:
                num = caps.find(symbol)
                num = num - key
                if num < 0:
                    num = num + len(letters)
                translated = translated + letters[num].upper()
            else:
                translated = translated + symbol
        print('Key #%s: %s ' % (key, translated))

def numtotext():
    num = input('ENTER MESSAGE: ').split(',')
    text = ''
    for i in range(len(num)):
        number = num[i]
        if number == " ' '":
            text += ' '
        else:
            letter = chr(int(number) + 97)
            text += str(letter)
    print(text)

def Ccnumtotext():
    num = input('ENTER MESSAGE: ').split(',')
    text = ''
    for i in range(len(num)):
        number = num[i]
        if number == " ' '":
            text += ' '
        else:
            letter = chr(int(number) + 97)
            text += str(letter)
    letters = 'abcdefghijklmnopqrstuvwxyz'
    for key in range(len(letters)):
        translated = ''
        for i in range(len(text)):
            symbol = text[i]
            if symbol in letters:
                num = letters.find(symbol)
                num = num - key
                if num < 0:
                    num = num + len(letters)
                translated = translated + letters[num]
            else:
                translated = translated + symbol
        print('Key #%s: %s ' % (key, translated))


def unscramble():
    dec = input('PLEASE CHOOSE YOUR DECRYPTION TYPE: \n\
[Cc] for Ceaser Decryption, \n\
[NT] for Number to Text, \n\
[CNT] for Number to Text + Ceaser Decryption: \n')

    if dec == 'Cc':
        DCcencrypt()
    elif dec == 'NT':
        numtotext()
    elif dec == 'CNT':
        Ccnumtotext()


which = input('[E]ncrypt or [D]ecrypt ')
if which == 'E':
    scramble()
elif which == 'D':
    unscramble()
