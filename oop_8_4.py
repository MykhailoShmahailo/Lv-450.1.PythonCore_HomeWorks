# 3.  Створити клас особа,  в якому конструктор встановлює ім’я, вік. Використати в цьому класі геттери та сеттери, 
# а також створити метод info, який виводить
# інформацію про ім’я та вік особи. А тоді створити клас працівник, 
# який наслідується від класу особи і містить метод details, який на вхід отримує параметр про компанію, 
# в якій працює працівник і цей метод виводить інформацію про те, що працівник з таким то іменем працює в такій то компанії.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print("Hello, my name is {} and my age is {}".format(self.name, self.age))


class Employee(Person):
    def __init__(self, company, name, age):
        Person.__init__(self, name, age)  #super().__init__(self, company) 
        self.company = company
    def details(self, company):
        print('The emloyee {} is working now in {}'.format(self.name, self.company))


p = Person("Alex", 12)
p.info()

d = Employee("IBM")
d.details()
