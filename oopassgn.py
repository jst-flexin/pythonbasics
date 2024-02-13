class fruits:
    def __init__(self,name,age,course):
        self.name = name
        self.age = age
        self.course = course


    def people(self):
        print(f"My name is {self.name} ,I am {self.age} years and I am taking {self.course}")
myintake=fruits("Flex",21,"Computer Science")
myintake.people()
myintake2=(fruits("Natasha",20,"Medicine"))
myintake2.people()
myintake3=fruits("Debbie",19,"Commerce")
myintake3.people()
myintake4=fruits("Duncan",24,"Education")
myintake4.people()
