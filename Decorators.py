"""
In Python, a decorator is a design pattern that allows you to modify the functionality of a function by wrapping it in another function.

The outer function is called the decorator, which takes the original function as an argument and returns a modified version of it.
I"""


def outer_func(func):
    def inner():
        print("I Got Decorated")
        func()
    return inner


@outer_func
def ordinary():
    print("I am Ordinary")

#Python Decorator with Argument

def do_twice(func):
    def wrapper_function(*args,**kwargs):
        func(*args,**kwargs)
        func(*args,**kwargs)
    return wrapper_function

@do_twice
def display(name):
      print("Hello {}" .format(name))

display(("Ramadevi,12345"))
ordinary()

###How it works
#ordinary = outer_func(ordinary)

#ordinary()  --> inner() --> "I Got Decorated" --> func() --> "I am Ordinary"


