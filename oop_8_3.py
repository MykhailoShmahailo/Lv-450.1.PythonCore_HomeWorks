# 2.  Створити клас особа,  в якому конструктор встановлює ім’я, 
# а метод info виводить повідомлення “Hello, my name is {ім’я конкретного екземпляра класу}”, а також створити клас автомобіль,  
# в якому конструктор встановлює ім’я, а метод move виводить повідомлення 
# {ім’я конкретного екземпляра класу}  moves at the speed {speed(цей параметр метод moveотримує як вхідний)} km / h

class Person:
    def __init__(self, name):
        self.name = name
    def info(self):
        print("Hello, my name is {}".format(self.name))


class Car:
    def __init__(self, name):
        self.name = name

    def speed(self, speed):
        self.speed = speed
        print("{} moves at the speed {} km/h".format(self.name, self.speed))    


p = Person("Alex")
p.info()

d = Car("Mercedes")
d.speed(12)