# ГЕНЕРАТОРЫ СПИСКОВ

print('Повторяем генераторы списков.')


print([x ** 3 for x in range(10) if x % 2 == 0])

print('-' * 100)

s = []

for i in range(1, 21):
    if i % 5 == 0:
        s.append(i)


s1 = [i for i  in range(1, 21)
        if i % 5 == 0]


print(f's = {s}; s1 = {s1}')

print('-' * 100)

def s_upper(string):
        for i in string:
                return i[0] == i[0].upper()

x = ['Denis',  'Dmitry', 'oleg', 'Dasha', 'jana']

print(list(filter(s_upper, x)))

#Альтернативное решение:
print('Альтернативное решение: ')

print([i for i in x if i[0] == i[0].upper()])


#Генераторы множеств и словарей
print('Генераторы множеств и словарей.')

q = 'Щербинин Денис Сергеевич'
res = {j for j in q}
print(f'В q = {q} длина строки = {len(q)}, res = {res}, а длина строки = {len(res)}')

char_position = {}

for elem, i in enumerate('Hello World'):
        print(f'Elem = {elem}, i = {i}')


print({i for i in [0, 1, 2, 3, 4, 1, 2, 4, 10, 1, 2, 5]})


print({i for i in ['a', 'b', 'c', 'a', 'b', 'c']})

print('-' * 100)

#Генератор словарей

print('-' * 50, 'Генератор словарей', '-' * 50)

dictionary = {i: i ** 2 for i in range(1, 6)}
print(f'Сгенерировали словарь - {dictionary}')
#Аналог:

dictionary2 = {}

for i in range(1, 6):
        dictionary2[i] = i ** 2

print(dictionary2)

print(f'Как видим: {dictionary} = {dictionary2}')

print('-' * 100)

word_len = {word: len(word) for word in ['Denis', 'Sherbinin', 'KIA']}

print(word_len)