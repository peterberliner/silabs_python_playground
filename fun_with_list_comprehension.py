import random

class Alien:
    def __init__(self):
        self.species = random.choice(['Zorgon', 'Bliptor', 'Xenon', 'Quarx'])
        self.num_eyes = random.randint(1, 8)
        self.home_planet = random.choice(['Mars', 'Venus', 'Jupiter', 'Neptune'])
        self.name:str = None
        self.is_friendly: bool = None

    def __repr__(self):
        return f"Alien(name={self.name}, {'friendly' if self.is_friendly else 'hostile'}, species='{self.species}', num_eyes={self.num_eyes}, home_planet='{self.home_planet}')"
    
# this does not work :()
# aliens = [(Alien(), print("adding alien"), aliens[i].name = Bob ) for i in range(5)]

aliens = [(Alien(), print("adding alien")) for i in range(5)]


for alien in aliens:
    print(alien)
