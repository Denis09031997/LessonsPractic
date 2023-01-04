# ДЕКЛАРАТИВНОЕ ПРОГРАММИРОВАНИЕ.


#Задача - вывести отсортированный список.

# ИМПЕРАТИВНОЕ РЕШЕНИЕ. Императивное программирование предполагает ответ на вопрос “Как?”.:

INPUT = [1, 2, 5, 3, 6, 4, 11, 84]

def main():
    numbers = INPUT[:]
    filter_and_sort(numbers)
    for number in numbers:
        print(number)
    
    return numbers


def filter_and_sort(values):
    values.sort()
    previous_value = None
    index = 0
    while index < len(values):
        value = values[index]
        if value == previous_value and index > 0:
            values.pop(index)
        else:
            index +=1
            previous_value = value


print(main())

print('-' * 100)

# ДЕКЛАРАТИВНОЕ РЕШЕНИЕ:

def main_declar():
    return list(map(str, sorted(set(INPUT))))

print(main_declar())