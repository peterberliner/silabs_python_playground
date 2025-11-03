class Spell_Type:
    MAGIC_MISSILE = "Magic Missile"
    DRAIN = "Drain"
    SHIELD = "Shield"
    POISON = "Poison"
    RECHARGE = "Recharge"

class Spell:
    def __init__(self, spell_type):
        self.cost = None
        self.damage = None
        self.heal = None
        self.lasts = None
        self.armor_increase = None
        self.mana_increase = None
        self.effects_instantly = False
        self.spell_type = spell_type

        if spell_type == Spell_Type.MAGIC_MISSILE:
            self.cost = 53
            self.damage = 4
            self.effects_instantly = True

        elif spell_type == Spell_Type.DRAIN:
            self.cost = 73
            self.damage = 2
            self.heal = 2
            self.effects_instantly = True

        elif spell_type == Spell_Type.SHIELD:
            self.cost = 113
            self.lasts = 6
            self.armor_increase = 7
            self.effects_instantly = True


        elif spell_type == Spell_Type.POISON:
            self.cost = 173
            self.damage = 3
            self.lasts = 6

        elif spell_type == Spell_Type.RECHARGE:
            self.cost = 229
            self.mana_increase = 101
            self.lasts = 5

    
