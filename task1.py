try:
    number1 = int(input('Enter first number: '))
    number2 = int(input('Enter second number: '))

    result = number1 / number2 
    print(result)

except ZeroDivisionError:
    print('Cannot divide by zero')

except ValueError:
    print('Invalid input')
