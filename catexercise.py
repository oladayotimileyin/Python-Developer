#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat("Amy", 4)
cat2 = Cat("Bella", 7)
cat3 = Cat("Charlie", 2)


# 2 Create a function that finds the oldest cat

def find_oldest_cat(cats):
    oldest_cat = cats[0]  # Start with the first cat as the oldest
    for cat in cats:
        if cat.age > oldest_cat.age:
            oldest_cat = cat
    return oldest_cat.age


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
cats = [cat1, cat2, cat3]
oldest_age = find_oldest_cat(cats)
print(f"The oldest cat is {oldest_age} years old.")


# Exercise Cats Everywhere

# Given the below class:

class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age

#Answers:
# 1 Instantiate the Cat object with 3 cats.
cat1 = Cat('cat1', 5)
cat2 = Cat('Cat2', 7)
cat3 = Cat('Cat3', 3)


# 2 Create a function that finds the oldest cat.
def oldest_cat(*args):
    return max(args)


# 3 Print out: "The oldest cat is x years old.".
# x will be the oldest cat age by using the function in #2
print(f'Oldest Cat is {oldest_cat(cat1.age, cat2.age, cat3.age)} years old.')




