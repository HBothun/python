from tkinter import *
from tkinter.font import BOLD
from PIL import Image, ImageTk

cipher = Tk()
cipher.title('Cipher')
cipher.iconbitmap('D:\VSCODE\Basics\GUI\Images\cipher.ico')
cipher.configure(background='mediumpurple3')

result= Text(cipher, 
    width=50, height=25,
    bg='mediumpurple4', fg='black',
    font=(BOLD, 15),
    wrap='word'
)

#### Encyrption ####

def Ccencrypt(x, y):
    text = str(x)
    s = int(y)
    global result
    punct = ['!', '?', "'", '"', '@', '.', ':', ';', '-', ',']
    for i in range(len(text)):
        char = text[i]
        if (char == ' '):
            result.insert(END, ' ')
        elif (char in punct):
            result.insert(END, char)
        elif (char.isupper()):
            result.insert(END, chr((ord(char) + s-65) % 26 + 65))
        else:
            result.insert(END, chr((ord(char) + s-97) % 26 + 97))
    return result

#### DECYRPTION ####

def DCcencrypt(x):
    global result
    punct = ['!', '?', "'", '"', '@', '.', ':', ';', '-', ',']
    for key in range(1, 26):
        if key == 1:
            result.insert(END, 'Key #%s: ' % (key))
        elif key > 1:
            result.insert(END, '\nKey #%s: ' % (key))
        for i in range(len(x)):
            char = x[i]
            if (char == ' '):
                result.insert(END, ' ')
            elif (char in punct):
                result.insert(END, char)
            elif (char.isupper()):
                result.insert(END, chr((ord(char) + key-65) % 26 + 65))
            else:
                result.insert(END, chr((ord(char) + key-97) % 26 + 97))
    return result

Label(cipher, 
    text='Message',
    font=BOLD,
    bg='mediumpurple3', fg='black', 
).grid(row=0, column=0, columnspan=4)
mes=Entry(cipher, 
    textvariable='', 
    bd=5, 
    bg='mediumpurple4', fg='black',
    font=BOLD
)
mes.grid(row=1, column=0, columnspan=4)

Label(cipher, 
    text='Shift',
    font=BOLD,
    bg='mediumpurple3', fg='black'
).grid(row=2, column=0, columnspan=4)
shf=Entry(cipher, 
    textvariable='',
    bd=5, 
    bg='mediumpurple4', fg='black',
    font=BOLD,
)
shf.grid(row=3, column=0, columnspan=4)


Button(cipher, 
    text='Encrypt', 
    command=lambda:Ccencrypt(mes.get(), shf.get()), 
    font=BOLD, 
    relief=RAISED, 
    bg='purple4', fg='green', 
    width= 15, height=0
).grid(row=4, column=0)
Button(cipher, 
    text='Decrypt', 
    command=lambda:DCcencrypt(mes.get()), 
    font=BOLD,
    relief=RAISED,  
    bg='purple4', fg='red3', 
    width=15, height=0
).grid(row=4, column=2)
Button(cipher,
    text='Clear',
    command=lambda: result.delete('1.0', END),
    bg='purple4', fg='white',
    font=(BOLD, 15),
    relief=RAISED
).grid(row=4, column=1)


result.grid(row=5, column=0, columnspan=3)



cipher.mainloop()