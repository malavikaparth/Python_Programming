# Passing function as an argument in Python
# A function can take multiple arguments, these arguments can be objects,
# variables(of same or different data types) and functions.
# Python functions are first class objects.
# In the example below, a function is assigned to a variable.
# This assignment doesn’t call the function.
# It takes the function object referenced by shout and creates a second name pointing to it, yell.

def shout(text):
    return text.upper()


print(shout("hello"))

yell = shout
print(yell("malavika"))


# Higher Order Functions
# Because functions are objects we can pass them as arguments to other functions.
# Functions that can accept other functions as arguments are also called higher-order functions.
# In the example below, a function greet is created which takes a function as an argument.

def sum(a, b):
    return a + b


def prod(a, b):
    return a * b


def combo(f, a, b):
    return f(a, b)


print(combo(sum, 2, 5))
print(combo(prod, 2, 5))


# Wrapper function
# Wrapper function or decorator allows us to wrap another function in order to extend the behavior
# of the wrapped function, without permanently modifying it.
# In Decorators, functions are taken as the argument into another function
# and then called inside the wrapper function.
# defining a decorator
def hello_decorator(func):
    # inner1 is a Wrapper function in
    # which the argument is called

    # inner function can access the outer local
    # functions like in this case "func"
    def inner1():
        print("Hello, this is before function execution")

        # calling the actual function now
        # inside the wrapper function.
        func()

        print("This is after function execution")

    return inner1


# defining a function, to be called inside wrapper
def function_to_be_used():
    print("This is inside the function !!")


# passing 'function_to_be_used' inside the
# decorator to control its behavior
function_to_be_used = hello_decorator(function_to_be_used)

# calling the function
function_to_be_used()
