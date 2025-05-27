#Assignment 1: Design Your Own Class
class Smartphone:
    def _init_(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage

    def make_call(self, number):
        print(f"{self.brand} {self.model} is calling {number}...")

    def install_app(self, app):
        print(f"{app} installed on {self.model}.")

#Inheritance Example
class Smartwatch(Smartphone):
    def _init_(self, brand, model, storage, strap_color):
        super()._init_(brand, model, storage)
        self.strap_color = strap_color

    def make_call(self, number):
        print(f"{self.model} (watch) is calling {number}...")

#Activity 2: Polymorphism Challenge
class Animal:
    def move(self):
        print("The animal moves.")

class Dog(Animal):
    def move(self):
        print("Running 🐕")

class Bird(Animal):
    def move(self):
        print("Flying 🕊️")

class Fish(Animal):
    def move(self):
        print("Swimming 🐟")

#Testing
phone = Smartphone("Samsung", "S22", "128GB")
phone.make_call("123-456")
watch = Smartwatch("Apple", "Watch Series 6", "32GB", "Black")
watch.make_call("987-654")

for animal in [Dog(), Bird(), Fish()]:
    animal.move()