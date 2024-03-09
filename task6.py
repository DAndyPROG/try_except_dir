def write_string(file_name):
    try:
        write_str = input('Напишіть фразу: ')
        with open(file_name, 'w') as file:
            file.write(write_str)
        print('Файл успішно записано!')

    except FileNotFoundError:
        print('Файл не знайдено!')

    except PermissionError:
        print('У вас недостатньо прав для запису в файл!')

if __name__ == '__main__':
    file_name = 'file6.txt'
    write_string(file_name)
