# Getters and Setters

- Getters and setters are special methods in object-oriented programming that allow you to control access to an object's attributes. They provide a way to encapsulate the internal state of an object and protect it from unauthorized access or modification.
- Getters are methods that retrieve the value of an attribute, while setters are methods that set or update the value of an attribute. They are often used to enforce data validation, maintain encapsulation, and provide a clear interface for interacting with an object's properties.
- Python uses the ``@property`` decorator so that name assumes getter behavior. Add the decorator and remove the inner parentheses from the print statement.
- Setters can also take the ``@property`` decorator, but its implementation is different from the getter. The setter decorator starts with a @ followed by the name of the getter method, and it ends with .setter. So if the getter is called name, the setter decorator is ``@name.setter``. The setter also has the same name as the getter, but its parameters are self and the new value.
- 