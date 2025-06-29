class example():
    def __init__(self):
        first = input()   # это - переменная, она используется только в рамках этой функции
        self.a = first   # это - переменная класса, она может использоваться везде
        self.b = input()   # это тоже переменная класса
        self.__c = 1   # это - закрытая переменная, ее можно достаь ТОЛЬКО через геттер и устуновить ТОЛЬКО через сеттер
    def first_method(self):   # это - метод (подфункция)
        print(self.a)   # выводим нашу переменную класса
    def second_method(self):
        print(self.b)
    def setter(self, q):   # это и есть тот самый сеттер
        self.__c = q
    def getter(self):   # а это - геттер
        return self.__c
object = example()   # создаем объект класса
print(object.b)   # достаем переменную класса
print(object.getter())   # достаем закрытую переменную класса
object.setter(3)      # назначаем закрытую переменную класса
print(object.getter())
