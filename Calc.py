def addition(x, y):
    return x + y

def subtration(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return (x / y)

def power(x, y):
    return x ** y

num1 = int(input('First Number: '))
operation = input('Operator: ')
num2 = int(input('Second Number: '))

if operation =='+':
    print(str(num1) + operation + str(num2) + ' = ' + str(addition(num1, num2)))
    num3 = (addition(num1, num2))
elif operation =='-':
    print(str(num1) + operation + str(num2) + ' = ' + str(subtration(num1, num2)))
    num3 = (subtration(num1, num2))
elif operation =='*':
    print(str(num1) + operation + str(num2) + ' = ' + str(multiply(num1, num2)))
    num3 = (multiply(num1, num2))
elif operation =='/':
    print(str(num1) + operation + str(num2) + ' = ' + str(divide(num1, num2)))
    num3 = (divide(num1, num2))
elif operation =='^':
    print(str(num1) + operation + str(num2) + ' = ' + str(power(num1, num2)))
    num3 = (power(num1, num2))
else:
    print('Operation Not Recognized \n\
        Please use: + - * / ^')

cont = input('Additional Operators? [Y/N] ')

if cont =='Y':
    operation2 = input('Operator: ')
    num4 = int(input('Third Number: '))
    if operation2 == '+' :
        print(str(num3) + operation2 + str(num4) + ' = ' + str(addition(num3, num4)))
    elif operation2 == '-' :
        print(str(num3) + operation2 + str(num4) + ' = ' + str(subtration(num3, num4)))
    elif operation2 == '*' :
        print(str(num3) + operation2 + str(num4) + ' = ' + str(multiply(num3, num4)))
    elif operation2 == '/' :
        print(str(num3) + operation2 + str(num4) + ' = ' + str(divide(num3, num4)))
    elif operation2 == '^' :
        print(str(num3) + operation2 + str(num4) + ' = ' + str(power(num3, num4)))
    else:
         print('Operation Not Recognized \n\
        Please use: + - * / ^')
    print('For More Operators Use a Real Calculator')
elif cont == 'N' :
    print('BYE')
