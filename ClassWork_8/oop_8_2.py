# 1.  Створити клас машина з атрибутами name,  make, model та методами start та stop, 
# які виводять інформацію про те що автомобіль стартував чи зупинився відповідно.


class Car: 
    def __init__(self, name, make, model):
        self.name = name
        self.make = make
        self.model = model
        print("Car is {} created {} and this model is {} ".format(self.name, self.make, self.model))

    def start(self):
        print("Engine {} is started".format(self.name))

    def stop(self):
        print("Engine {} is stopped".format(self.name))


p = Car("Audi", 1996, "A6")
p.start()
d = Car("BMW", 2001, "X5")
d.stop()