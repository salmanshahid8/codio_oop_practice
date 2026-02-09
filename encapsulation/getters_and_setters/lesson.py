# basic getter and setter methods
class TestClass:
    def __init__(self, num1, num2):
        self._num1 = num1
        self._num2 = num2
        self._sum = 0

    def get_num1(self):
        return self._num1

    def set_num1(self, new_value):
        self._num1 = new_value

    def get_num2(self):
        return self._num2

    def set_num2(self, new_value):
        self._num2 = new_value

    def get_sum(self):
        return self._sum

    def set_sum(self, new_value):
        self._sum = new_value


class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name


# # Alternative implementation of the Person class
# class Person:
#     def __init__(self, name):
#         self._name = name

#     def get_name(self):
#         return self._name

#     def set_name(self, new_name):
#         self._name = new_name

#     name = property(get_name, set_name)


if __name__ == "__main__":
    obj = TestClass(5, 7)
    print(obj.get_num1())
    print(obj.get_num2())
    obj.set_sum(obj.get_num1() + obj.get_num2())
    print(obj.get_sum())

    c = Person("Calvin")
    print(c.name)
    c.name = "Hobbes"
    print(c.name)
