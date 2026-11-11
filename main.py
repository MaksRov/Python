# базовый класс
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("У каждого животного свой звук")


# наследник
class Cat(Animal):
    def speak(self):
        return "Мяу"


class Dog(Animal):
    def speak(self):
        return "Мяу"

# Использование
animals = [Cat("Барсик"), Dog("Рекс")]
for a in animals:
    print(f"{a.name}: {a.speak()}")
# Барсик: Мяу
# Рекс: Гав