try:
    f = open("file.txt", "r")
except FileNotFoundError:
    print("Файл не знайдено!")
else:
    print("Файл прочитано!")
    f.close()
    print("Файл закрито!") 
