import random

class Hat:
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod
    def sort(cls, name):
        if not name:
            raise ValueError("Name cannot be empty")
        # return f"{name} has been sorted into {self.houses[hash(name) % len(self.houses)]}!"
        return f"{name} has been sorted into {random.choice(cls.houses)}!"

print(Hat.sort("Harry"))
