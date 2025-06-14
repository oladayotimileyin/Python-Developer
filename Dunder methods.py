## dunder methods
class Toy():
    def __init__(self, colour, age):
        self.colour = colour
        self.age = age

    ## modify __str__
    def __str__(self):
        return f"Toy colour: {self.colour}, Age: {self.age}"
    
    ## modify __del__
    def __del__(self):
        print("Toy deleted")

    ## __call__ allows an instance of the class to be called as a function
    def __call__(self):
        return ('yes , I am callable!')

action_figure = Toy("red", 2)

print(action_figure.__str__())
print(str(action_figure))

print(action_figure.__str__())
del(action_figure)

print(action_figure())