#initiate a class
class employee:
    #method/function/constructor
    def __init__(self):
        
        self.id = 123
        self.salary = 50000
        self.designation = "SDE"

    def travel(self, destination):
        print(f"Employee is travelling to {destination}")

#initiate an object/instance
sam = employee()

#print(sam.id)
sam.travel("Mumbai")
