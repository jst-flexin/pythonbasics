class fruits:
    def __init__(self,name,price,colour):
        self.name = name
        self.price = price
        self.colour = colour
    def malisaa(self):
        print(f"My favourite fruit is {self.name} and it costs Ksh. {self.price} and it is {self.colour} in colour.")

myobj=fruits("Orange",50,"orange")
myobj.malisaa()

myobj2=fruits("Banana",25,"yellow")
myobj2.malisaa()


class Persons:
    def __init__(self,name,age)
