from functools import wraps

def decorator(func):
    print(id(func))

    @wraps(func) #Чтобы не пропала документация функции
    def inner(name): # ВЗЯТЬ ЗА ПРАВИЛО - НЕ ВАЖНО СКОЛЬКО И ЕСТЬ ЛИ АРГУМЕНТЫ ВООБЩЕ, ВСЕГДА 
        #ЛУЧШЕ ПРОПИСЫВАТЬ ЧЕРЕЗ *ARGS И **KWARGS
        print('Щас начнется декоратор!')
        func(name)
        print('Декоратор окончен, расходимся ребята')

    return inner

@decorator
def say(name):
    print('А это вот и есть отдельная функция в декорировании.', name)


say('Дэнчик')
print('-' * 100)

@decorator
def by(name):
    print('Ну быдь здоров!', name)


by("Дениииииииииис")

print('Имя функции say -', say.__name__, 'by - ', by.__name__, 'decorator - ', decorator.__name__)

print('-' * 100)


@decorator
def sqr(x):
    """
    Функция возведения в квадрат
    """
    print(x ** 2)

sqr(12)


