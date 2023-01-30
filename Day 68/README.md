# Collections.UserList
Python supports a List like a container called UserList present in the collections module. This class acts as a wrapper class around the List objects. This class is useful when one wants to create a list of their own with some modified functionality or with some new functionality. It can be considered as a way of adding new behaviors for the list. This class takes a list instance as an argument and simulates a list that is kept in a regular list. The list is accessible by the data attribute of the this class.

## Syntax:
```
collections.UserList([list])
```

## Program Output
```
Original List
After Insertion
[1, 2, 3, 4, 5]
```
```
Traceback (most recent call last):
  File "/home/9399c9e865a7493dce58e88571472d23.py", line 33, in 
    L.remove()
  File "/home/9399c9e865a7493dce58e88571472d23.py", line 15, in remove
    raise RuntimeError("Deletion not allowed")
RuntimeError: Deletion not allowed
```
