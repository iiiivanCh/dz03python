# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def get_user_number(str_1):
    while True:
        try:
            num = int(input(str_1))
            return num
        except ValueError:
            print("Вы ввели не целое число. Повторите ввод")


def get_convert_decimal_binary(num):
    num_binary = ""
    while num != 0:
        num_binary = str(num % 2) + num_binary
        num //= 2
    print(num_binary)


user_number = get_user_number(
    'Введите десятичное число для преобразования его в двоичное: ')
get_convert_decimal_binary(user_number)
