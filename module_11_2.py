import inspect

class MyClass:
    def __init__(self, value):
        self.value = value

    def add(self, amount):
        return self.value + amount

    def greet(self):
        return f"Hello, your value is {self.value}"

def introspection_info(obj):
    info = {
        'type': type(obj).__name__,
        'attributes': [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")],
        'methods': [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith("__")],
        'module': obj.__module__,
        'is_instance': isinstance(obj, object)
    }
    return info

my_object = MyClass(42)

object_info = introspection_info(my_object)
print(object_info)