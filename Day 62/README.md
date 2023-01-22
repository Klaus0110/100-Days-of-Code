# Namedtuple in Python
Python supports a type of container dictionaries called “namedtuple()” present in the module, “collections“. Like dictionaries, they contain keys that are hashed to a particular value. But on contrary, it supports both access from key-value and iteration, the functionality that dictionaries lack.

## Access Operations
* Access by index: The attribute values of namedtuple() are ordered and can be accessed using the index number unlike dictionaries which are not accessible by index.
* Access by keyname: Access by keyname is also allowed as in dictionaries.
* using getattr(): This is yet another way to access the value by giving namedtuple and key value as its argument.

## Conversion Operations
* _make() :- This function is used to return a namedtuple() from the iterable passed as argument.
* _asdict() :- This function returns the OrderedDict() as constructed from the mapped values of namedtuple().
* using “**” (double star) operator :- This function is used to convert a dictionary into the namedtuple().

## Additional Operation 
* _fields: This function is used to return all the keynames of the namespace declared.
* _replace(): _replace() is like str.replace() but targets named fields( does not modify the original values)
