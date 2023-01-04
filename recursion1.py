def math(x):
    if x > 100:
        return x
    print(f'X = {x}')
    math(x * 2)


print(math(2))

print('-' * 100)

def some(num):
    if num <= 1:
        return 1
    else:
        return num * some(num - 1)

print(some(8))

print('-' * 100)


#Создадим функцию, которая отбирает четные числа - без рекурсии, при помощи обычного цикла.

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

print('Функция без рекурсии:')
def func(l):
    result = []
    for i in l:
        if i % 2 == 0:
            result.append(i)
    
    return result


print(func(x))
print('-' * 100)

# Теперь такая же функция, но при помощи рекурсии:
print('Функция с рекурсией:')


def recursion_func(lst, result = []):
    if not lst:
        return
    else:
        first_elem = lst[0]
        if first_elem % 2 == 0:
            result.append(first_elem)
        recursion_func(lst[1:])

        return result

print(recursion_func(x))

# Рекурсия в некоторых случая помогает писать короткий и читаемый код. Каждая задача, разбивается на подзадачу - если при помощи рекурсии 
#решен один кусочек задачи - то остальные можно считать также решены. Хороший пример  - решение задачи чисел Фибоначчи.
