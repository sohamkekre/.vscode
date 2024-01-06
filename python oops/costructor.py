class from_trees:
    def __init__(self,name,color) -> None:
        self.name = name
        self.color = color
    def __str__(self) -> str: #this function is a special __str__ function which helps us when we call print function with an instance of our class
        return (f"This fruit is {self.name} and its color is {self.color}")
        
    def fruits(self):
        print(f"You asked for a {self.name}")
        print(f"Your fruit's color is {self.color}\n")


fruit = from_trees("pinapple","yellow")
# fruit.name = "pinapple"
print(fruit)
fruit.fruits()


fruit1 = from_trees("apple","red")
# fruit1.name = "apple"
fruit1.fruits()

class Person:
  def __init__(self, name):
    self.name = name
  def greeting(self):
    """Outputs a message with the name of the person (this is known as docstring and this tells us about the function or class or method etc it is not same as comment)"""
    print("Hello! My name is {name}.".format(name=self.name)) 

help(Person.greeting)