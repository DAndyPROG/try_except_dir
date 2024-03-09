def compare_files(file_1, file_2):
    try:
        with open(file_1, 'r') as file:
            line_file1 = set(file.readlines())
        
        with open(file_2, 'r') as file:
            line_file2 = set(file.readlines())
        
        unique_lines = line_file1 - line_file2

        for line in unique_lines:
            print(line.strip())
        

    except FileNotFoundError:
        print('Файл не знайдено')


compare_files('file1.txt', 'file2.txt')
            