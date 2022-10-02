# Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


def get_user_number(str_1):
    while True:
        try:
            num = int(input(str_1))
            return num
        except ValueError:
            print("Вы ввели не целое число. Повторите ввод")


def get_fibonacci(num):
    fibo_num = []
    a, b = 0, 1
    for i in range(num + 1):
        fibo_num.append(a)
        a, b = b, a + b
    return fibo_num


def get_negafibonacci(num):
    negafib_num = []
    for i in range(1, len(num)):
        negafib_num.append(num[i] * (-1) ** (i + 1))
    negafib_num.reverse()
    return negafib_num


series = get_user_number("Введите длину ряда: ")
fib = get_fibonacci(series)
negafib = get_negafibonacci(fib)
negafib.extend(fib)
print(negafib)
