# PYTHON UNITTEST FOR PROJECT

All unittest for each module created

### Model for all unittests

- *All test files are python files (extension: .py)*
- *All test files and folders start with test_*
- *File organization in the tests folder are the same as in the project*
- *e.g., For models/base_model.py, unit tests is in: tests/test_models/test_base_model.py*
- *e.g., For models/user.py, unit tests is in: tests/test_models/test_user.py*
- *All tests are executed by using this command: python3 -m unittest discover tests*
- *Testing file by file can be initiated by using this command: python3 -m unittest tests/test_models/test_base_model.py*
- *All classes have a documentation: (python3 -c 'print(__import__("my_module").MyClass.__doc__)')*
- *All functions (inside and outside a class) have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')*
