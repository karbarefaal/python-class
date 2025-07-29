from collections import UserDict

class MyCustomDict(UserDict):
    def __setitem__(self, key, value):
        print(f"Setting key '{key}' to value '{value}'")
        super().__setitem__(key, value)

    def __getitem__(self, key):
        print(f"Accessing key '{key}'")
        return super().__getitem__(key)
    
    def sayHello(self):
        return "salam salam"

# Create an instance of the custom dictionary
d = MyCustomDict()
d['name'] = 'Alice'  # Output: Setting key 'name' to value 'Alice'
print(d['name'])     # Output: Accessing key 'name' \n Alice
print(d.sayHello)