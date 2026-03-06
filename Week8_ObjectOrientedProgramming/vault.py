class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0, password=""):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts
        self.password = password
    
    def open(self, password):
        if password == self.password:
            return "Vault opened!"
        else:
            return "Incorrect password."
        
    def __str__(self):
        return f"Vault with {self.galleons} galleons, {self.sickles} sickles, and {self.knuts} knuts."

    def __add__(self, other):
        if isinstance(other, Vault):
            total_galleons = self.galleons + other.galleons
            total_sickles = self.sickles + other.sickles
            total_knuts = self.knuts + other.knuts
            return Vault(galleons=total_galleons, sickles=total_sickles, knuts=total_knuts)
        return NotImplemented
        
potter = Vault(galleons=100, sickles=50, knuts=25, password="accio")
print(potter.open("accio"))  # Vault opened!
print(potter)  # Vault with 100 galleons, 50 sickles, and 25 knuts.

weasley = Vault(galleons=25, sickles=50, knuts=100, password="wingardium")
print(weasley)  # Vault with 200 galleons, 100 sickles, and 50 knuts.

galleons = potter.galleons + weasley.galleons
sickles = potter.sickles + weasley.sickles
knuts = potter.knuts + weasley.knuts
print(f"Total: {galleons} galleons, {sickles} sickles, and {knuts} knuts.")  # Total: 125 galleons, 100 sickles, and 125 knuts.

total = Vault(galleons=galleons, sickles=sickles, knuts=knuts)
print(total)  # Vault with 125 galleons, 100 sickles, and 125 knuts.

total = potter + weasley
print(total)  # Vault with 125 galleons, 100 sickles, and 125 knuts.

print (potter + 5)  # NotImplemented
