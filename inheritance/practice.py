class Pet:
    def __init__(self, name):
        self.name = name


class Dog:
    def __init__(self, name, breed):
        self.name = name

    def bark(self):
        print("Woof! Woof!")


class Pug(Dog):
    def bark(self):
        super().bark()
