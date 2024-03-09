# Реалізуйте програму, яка копіює вміст одного файлу в інший.

def copy_file_text(file1, file2): 
    try:
        with open(file1, 'r') as f1:
            with open(file2, 'w') as f2:
                for line in f1:
                    f2.write(line)
                    f2.write('\n')
                
                f1.close()
                f2.close()
    
    except FileNotFoundError:
        print('Файл не знайдено')

if __name__ == '__main__':
    copy_file_text('file3.txt', 'file4.txt')

