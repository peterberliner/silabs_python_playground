class Fighter():
    def __init__(self, name, hit_points, mana=0, armor=0, damage=0):
        self.name = name
        self.hit_points = hit_points
        self.mana = mana
        self.armor = armor
        self.extra_armor = 0  # Additional armor from spells or effects
        self.damage = damage
        
    