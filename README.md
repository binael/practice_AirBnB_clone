# AirBnB clone - The console

![AirBnB](hng.png)

## Project Description
The goal of the project is to deploy a simple copy of the AirBnB website as the first ALX project on full web application. The command intepreter will be used to manage the AirBnB objects

### The project is broken down into several tasks:
- _creating a parent class *(called BaseModel)* to take care of the initialization, serialization and deserialization of your future instances_
- _creating a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file_
- _creating all classes used for AirBnB (User, State, City, Place, Amenities, Reviews) that inherit from BaseModel_
- _creating the first abstracted storage engine of the project: File storage._
- _creating all unittests to validate all our classes and storage engine_

### Learning Objectives
- _How to create a Python package_
- _How to create a command interpreter in Python using the cmd module_
- _What is Unit testing and how to implement it in a large project_
- _How to serialize and deserialize a Class_
- _How to write and read a JSON file_
- _How to manage datetime_
- _What is an UUID_
- _What is *args and how to use it_
- _What is **kwargs and how to use it_
- _How to handle named arguments in a function_

### Files

 -  HBNHCommand: console.py
 -  Amenity: models/amenity.py
 -  BaseModel: models/base_model.py
 -  City: models/city.py
 -  models.init : models/__init__.py
 -  Place: models/place.py
 -  Review: models/review.py
 -  State: models/state.py
 -  User: models/user.py
 -  FileStorage: models/engine/file_storage.py
 -  engine.init: models/engine/__init__.py

 ## How the command intepreter manages the AirBnB Objects
- _Create a new object (ex: a new User or a new Place)_
- _Retrieve an object from a file, a database etc…_
- _Do operations on objects (count, compute stats, etc…)_
- _Update attributes of an object_
- _Destroy an object_

### Execution
*Your shell should work like this in interactive mode:*
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
```

*But also in non-interactive mode: (like the Shell project in C)*
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```

All tests should also pass in non-interactive mode: *$ echo "python3 -m unittest discover tests" | bash*

![console](console.png)

## AUTHORS:

- *Binael Nchekwube* - [Binael](https://github.com/binael)
- *Lema Kefyalew* - []()
