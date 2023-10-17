# Self is always pointing to Current Object.
# Self is the first argument to be passed in Constructor and Instance Method.
# self is parameter in Instance Method and user can use another parameter name in place of it.
# But it is advisable to use self because it increases the readability of
# code, and it is also a good programming practice.

class check:
    def __init__(self):
        print("Address of self", id(self))


checkObj = check()
print("Address of  object: ", id(checkObj))


# OUTPUT:
# it is clearly seen that self and obj is referring to the same object
# Address of self 2035333773248
# Address of  object:  2035333773248

# EG 2
class car():

    # init method or constructor
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def show(self):
        print("Model is", self.model)
        print("color is", self.color)
        print("Address of object", id(self))


# both objects have different self which
# contain their attributes
audi = car("audi a4", "blue")
ferrari = car("ferrari 488", "green")

audi.show()  # same output as car.show(audi)
ferrari.show()  # same output as car.show(ferrari)
print("audi id", id(audi))  # These are same as there corresponding self
print("ferrari id", id(ferrari))


# Behind the scene, in every instance method
# call, python sends the instances also with
# that method call like car.show(audi)

# EG3 : replacing self with another keyword
class this_is_class:
    def __init__(replacement_for_self):
        print("we have used another "
        "parameter name in place of self", id(replacement_for_self))
        replacement_for_self.n = 1

    def addN(replacement_for_self1):
        replacement_for_self1.n = 2

    def display(replacement_for_self3):
        print(replacement_for_self3.n)


a = this_is_class()
a.addN()
a.display()
