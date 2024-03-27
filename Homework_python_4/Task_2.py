# Задача_2
# Напишите функцию принимающую на вход только ключевые параметры и 
# возвращающую словарь, где ключ — значение переданного аргумента,
# а значение — имя аргумента. Если ключ не хешируем, используйте
# его строковое представление


def create_dict(**kwargs):
    result = {}
    for key,value in kwargs.items():
        if hash(value):
            result[value]= key
        else:
            result[str(value)]= key
    return result


print(create_dict(a=2345,b=34,c='3sff',d=23))

