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