class material:
    def __init__(self,color,fabric) -> None:
        self.color = color
        self.fabric = fabric
    def __str__(self) -> str:
        return("you didnt call your object with specific method please call it with a method")
    def about(self):
        print(f"your material {self.color} in color and its fabric is {self.fabric}" )

sweater = material("red","cotton")
# sweater.about()
print(sweater)