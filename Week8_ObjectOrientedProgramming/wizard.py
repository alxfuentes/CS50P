class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Name cannot be empty")
        self.name = name

    ...
    
class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house
    
    ...
            
class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
        
    ...

wizard = Wizard("Albus Dumbledore")
print(wizard.name)  # Albus Dumbledore
    
student = Student("Harry", "Gryffindor")
print(student.name)  # Harry
print(student.house)  # Gryffindor  

professor = Professor("Dumbledore", "Transfiguration")
print(professor.name)  # Dumbledore
print(professor.subject)  # Transfiguration

professor2 = Professor("Snape", "Potions")
print(professor2.name)  # Snape 
print(professor2.subject)  # Potions
