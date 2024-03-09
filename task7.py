try:
    my_list = [1,3,4,5,6,7,8,9,10,11]

    for i in range(1,len(my_list)):
        print(my_list[i])
 
    
except IndexError:
    print("Помилка: Неправильний індекс списку")

else:
    print("Програма успішно завершена")