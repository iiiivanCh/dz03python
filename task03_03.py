# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между
# максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

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
        arr_list.append(round(random.uniform(0, 10), 2))
    print(arr_list, end=' -> ')
    return arr_list


def get_getting_balance(arr):
    user_arr = []
    for i in arr:
        user_arr.append(round(i - int(i), 2))
    return user_arr


def get_difference_between_max_min(arr):
    arr_max = arr[0]
    arr_min = arr[0]
    for i in arr[1:]:
        if i > arr_max:
            arr_max = i
        if i < arr_min:
            arr_min = i
    print(
        f'Максимальный остаток: {arr_max}, минимальный остаток: {arr_min}, разница: {arr_max - arr_min}')


user_len = get_user_number('Задайте длину списка (массива): ')
user_list = get_user_random_list(user_len)
user_list_remains = get_getting_balance(user_list)
get_difference_between_max_min(user_list_remains)
