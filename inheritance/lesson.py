# Parent class


class Person:
    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation

    def say_hello(self):
        print(f"Hello, my name is {self.name}.")

    def say_age(self):
        print(f"I am {self.age} years old.")


# Child class
class Superhero(Person):
    def __init__(self, name, age, occupation):
        super().__init__(name, age, occupation)

    def say_hello(self):
        super().say_hello()


if __name__ == "__main__":
    hero = Superhero("Scarlet Witch", 32, "red balls")
    hero.say_hello()
    print(isinstance(hero, Superhero))
    print(isinstance(hero, Person))

    print(issubclass(Superhero, Person))
    print(issubclass(Person, Superhero))
