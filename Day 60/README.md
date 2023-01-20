# DefaultDict in Python
Defaultdict is a container like dictionaries present in the module collections. Defaultdict is a sub-class of the dictionary class that returns a dictionary-like object. The functionality of both dictionaries and defaultdict are almost same except for the fact that defaultdict never raises a KeyError. It provides a default value for the key that does not exists.

```
Syntax:
defaultdict(default_factory)

Parameters:  
default_factory: A function returning the default value for the dictionary defined.
If this argument is absent then the dictionary raises a KeyError.
```

## Inner Working
Defaultdict adds one writable instance variable and one method in addition to the standard dictionary operations. The instance variable is the default_factory parameter and the method provided is __missing__.

* __Default_factory__ : It is a function returning the default value for the dictionary defined. If this argument is absent then the dictionary raises a KeyError.
* __missing__(): This function is used to provide the default value for the dictionary. This function takes default_factory as an argument and if this argument is None, a KeyError is raised otherwise it provides a default value for the given key. This method is basically called by the __getitem__() method of the dict class when the requested key is not found. __getitem__() raises or return the value returned by the __missing__(). method.
