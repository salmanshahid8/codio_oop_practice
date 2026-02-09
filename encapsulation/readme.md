# Encapsulation

- Encapsulation is a fundamental principle of object-oriented programming (OOP) that involves bundling data and methods that operate on that data within a single unit, typically a class. It restricts direct access to some of an object's components, which can help prevent unintended interference and misuse of the data.
- The single underscore is a convention. That is, an informal agreement to recognize that attributes and methods with a single underscore are private. The Python interpreter does not enforce any restrictions that make these attributes private.
- Using two underscores, however, causes the Python interpreter to enforce changes.
- When the Python interpreter encounters an attribute with a double underscore, it does not make it private. Instead, it changes the name to ``_ClassName__AttributeName``. That is why Python returns and error for ``print(obj.__private_attribute).__private_attribute`` does not exist. It has been renamed to ``_PrivateClass__private_attribute``. This whole process is called name mangling, and it is designed to avoid name collisions in inheritance.
