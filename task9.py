def count_words(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()
            words = text.split()
            word_count = len(words)
            print(f"Кількість слів у файлі '{filename}': {word_count}")
    except FileNotFoundError:
        print(f"Файл '{filename}' не знайдено.")
    except IOError:
        print(f"Помилка при зчитуванні файлу '{filename}'.")

filename = input("Введіть назву файлу: ")
count_words(filename)