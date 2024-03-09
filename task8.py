def lst_numbers():
    try:
        input_numbers = input('Введіть список чисел, розділяючи їх комами: ').split(',')
        
        numbers = list(map(int, input_numbers))
        for number in input_numbers:
            
            print(f'Введене число: {number}')
        
        index = int(input('Введіть індекс елементу: '))
        value = numbers[index]
        print(f'Введене число: {value} : {index}')
    
    except ValueError:
        print('Невірно введене значення!')
    
    except IndexError:
        print('Помилка: Неправильний індекс списку')


lst_numbers()
