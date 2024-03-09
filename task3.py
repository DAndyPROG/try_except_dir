try:
    number1 = input('Введіть перше число: ') 
    number2 = int(input('Введіть друге число: '))

    print(number1 + number2)

except TypeError:
    print('Невірний тип даних!')

except ValueError:
    print('Невірно введене значення!')
