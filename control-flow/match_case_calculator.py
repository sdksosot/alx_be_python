num1 = int(input("Enter the first number: "))
num2 = int(input('Enter the second number: '))
type = input( 'Choose the operation (+, -, *, /): ')
match type:
    case '+':
        print(f'The result is [{num1 + num2}]' )
    case _ if num2 == 0 and type == '/':
        print('Cannot divide by zero.')
    case _ if num2 != 0 and type == '/':
        print(f'The result is [{num1 / num2}]')
    case "-":
        print(f'The result is [{num1 - num2}]' )
    case "*":
        print(f'The result is [{num1 * num2}]' )