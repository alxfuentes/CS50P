class Student:
    def __init__(self, name, house, patronus=None):
        self.name = name
        self.house = house
        self.patronus = patronus

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        self._name = value

    @property
    def house(self):
        return self._house
    
    @house.setter
    def house(self, value):
        if value not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = value

    def __str__(self):
        return f"{self.name} from {self.house}"

    def charm(self):
        if self.patronus:
            match self.patronus.lower():
                case "stag":
                    return f"{self.name} casts a stag patronus!"
                case "otter":
                    return f"{self.name} casts an otter patronus!"
                case "hare":
                    return f"{self.name} casts a hare patronus!"
                case _:
                    return "🪄"
        else:
            return f"{self.name} has no patronus to cast."

    
def main():
    student = get_student()
    print(student)
    print(student.charm())
    
def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus (optional): ")
    return Student(name, house, patronus)

if __name__ == "__main__":
    main()
