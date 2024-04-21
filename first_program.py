from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# Instantiate objects of the concrete classes
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Call the abstract method without knowing its implementation details
print(dog.make_sound())  # Output: Woof!
print(cat.make_sound())  # Output: Meow!


