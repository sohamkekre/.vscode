from abc import ABC, abstractmethod

class university(ABC):
    @abstractmethod
    def rules(self,name):
        pass
    # so what happenning here is we have declared the rules method in this class as the abstract method using the method decorator so even if implement this method and then use it we will get the error "cant instantiate abstract class with abstract method rules" so after implementing the method we have to remove that decorator to make it normal method.

class SVVV(university):
    def rules(self):
        print("We have strict rules")


s1 = SVVV()

s1.rules()

