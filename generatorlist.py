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