"""
line 1: define a very simple class...
lines 3 through 10: ... and fill it with some attributes;
line 12: this is our function!
line 13: scan the __dict__ attribute, looking for all attribute names;
line 14: if a name starts with i...
line 15: ... use the getattr() function to get its current value; note: getattr() takes two arguments: an object, and its property name (as a string), and returns the current attribute's value;
line 16: check if the value is of type integer, and use the function isinstance() for this purpose (we'll discuss this later);
line 17: if the check goes well, increment the property's value by making use of the setattr() function; the function takes three arguments: an object, the property name (as a string), and the property's new value.
"""
class MyClass:
        pass


obj = MyClass()
obj.a = 1
obj.b = 2
obj.i = 3
obj.ireal = 3.5
obj.integer = 4
obj.z = 5
    

def incIntsI(obj):
        for name in obj.__dict__.keys():
            if name.startswith('i'):
                    val = getattr(obj, name)
                    if isinstance(val, int):
                            setattr(obj, name, val + 1)

                    
print(obj.__dict__)
incIntsI(obj)
print(obj.__dict__)
                                                                        
