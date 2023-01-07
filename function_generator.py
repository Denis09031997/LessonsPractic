#ФУНКЦИИ-ГЕНЕРАТОРЫ

def f():
    return [30, 40, 50]


def genf():
    for i in [20, 30, 50]:
        yield i


print(f())

print('-----------------------')

s = genf()

print(s)
print(next(s))
print(next(s))
print(next(s))
print('-' * 30)

for i in genf():
    print(i)

print('-' * 100)
#Пример с факториалом

def fact(n):
    pr = 1
    for i in range(1, n + 1):
        pr = pr * i
        yield pr


a = fact(10)

print(next(a))
print(next(a))
print(next(a))
print(next(a))

print('-' * 100)

def d(iter):
    for i in iter:
        yield i


j = d('Denis')

print(next(j))
print(next(j))
print(next(j))
print(next(j))
print(next(j))

print('-' * 100)

def test():
    print('Понеслась!')
    while True:
        yield 1
        yield 2

q = test()

print(next(q))
print(next(q))
print(next(q))
print(next(q))
print(next(q))
print(next(q))
print(next(q))
print(next(q))