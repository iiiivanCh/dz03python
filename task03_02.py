# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random


def get_user_number(str_1):
    while True:
        try:
            num = int(input(str_1))
            return num
        except ValueError:
            print("Вы ввели не целое число. Повторите ввод")


def get_user_random_list(arr_len):
    arr_list = []
    for i in range(arr_len):
        arr_list.append(random.randint(0, 10))
    print(arr_list, end=' -> ')
    return arr_list


def get_product_pairs_list_number(arr):
    arr_new = arr[:]
    arr_list = []
    while len(arr_new) > 0:
        if len(arr_new) > 1:
            first = arr_new.pop(0)
            second = arr_new.pop(-1)
            arr_list.append(first * second)
        else:
            arr_list.append(arr_new.pop(0) ** 2)
    print(arr_list)


user_len = get_user_number('Задайте длину списка (массива): ')
user_list = get_user_random_list(user_len)
get_product_pairs_list_number(user_list)
