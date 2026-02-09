# Class with all public attributes and methods
class PublicPhone:
    def __init__(self, make, storage, megapixels):
        self.make = make
        self.storage = storage
        self.megapixels = megapixels


class PrivatePhone:
    def __init__(self, model, storage, megapixels, carrier):
        self._model = model
        self._storage = storage
        self._megapixels = megapixels
        self._carrier = carrier


class PrivateClass:
    def __init__(self):
        self.__private_attribute = "I am a private attribute"

    def helper_method(self):
        return self.__private_attribute


if __name__ == "__main__":
    public_phone = PublicPhone("iPhone", 256, 12)
    print(public_phone.storage)
    public_phone.storage = 64
    print(public_phone.storage)
    private_phone = PrivatePhone("iPhone", 256, 12, "Verizon")
    print(private_phone.__dict__)
    obj = PrivateClass()
    print(obj.helper_method())
    # print(obj.__private_attribute)  # This will raise an AttributeError
