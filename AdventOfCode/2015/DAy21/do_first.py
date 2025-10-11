my_hit_points = 100
boss_hit_points = 108
boss_armour = 2
boss_damage = 8

class fightItem():
    def __init__(self, name, cost, damage, armor):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.armor = armor

class attack_inventory_option():
    def __init__(self, weapon : fightItem, ring1:fightItem, ring2:fightItem):
        self.weapon = weapon
        self.ring1 = ring1
        self.ring2 = ring2

        self.tworings =  (ring1 is not None) and (ring2 is not None)

        self.total_cost = (weapon.cost if weapon else 0) + (ring1.cost if ring1 else 0) + (ring2.cost if ring2 else 0)
        self.total_damage = (weapon.damage if weapon else 0) + (ring1.damage if ring1 else 0) + (ring2.damage if ring2 else 0)
        self.cost_per_hit = 0
        if self.total_damage > boss_armour:
            self.cost_per_hit = self.total_cost / (self.total_damage - boss_armour)
        else :
            self.cost_per_hit = self.total_cost

class defend_inventory_option():
    def __init__(self, armor : fightItem, ring1:fightItem, ring2:fightItem):
        self.armor = armor
        self.ring1 = ring1
        self.ring2 = ring2

        self.tworings =  (ring1 is not None) and (ring2 is not None)

        self.total_cost = (armor.cost if armor else 0) + (ring1.cost if ring1 else 0) + (ring2.cost if ring2 else 0)
        self.total_armour = (armor.armor if armor else 0) + (ring1.armor if ring1 else 0) + (ring2.armor if ring2 else 0)
        effective_armour = boss_damage - self.total_armour if boss_damage - self.total_armour > 0 else 1
        self.cost_per_deflect = self.total_cost / effective_armour

weapons = [
    None,
    fightItem("Dagger", 8, 4, 0),
    fightItem("Shortsword", 10, 5, 0),
    fightItem("Warhammer", 25, 6, 0),
    fightItem("Longsword", 40, 7, 0),
    fightItem("Greataxe", 74, 8, 0)
]

attack_rings = [
    None,
    fightItem("Damage +1", 25, 1, 0),
    fightItem("Damage +2", 50, 2, 0),
    fightItem("Damage +3", 100, 3, 0)
]

armors = [
    None,   
    fightItem("Leather", 13, 0, 1),
    fightItem("Chainmail", 31, 0, 2),
    fightItem("Splintmail", 53, 0, 3),
    fightItem("Bandedmail", 75, 0, 4),
    fightItem("Platemail", 102, 0, 5)
]

armor_rings = [
    None,
    fightItem("Defense +1", 20, 0, 1),
    fightItem("Defense +2", 40, 0, 2),
    fightItem("Defense +3", 80, 0, 3)
]

attack_options = []
for weapon in weapons:
    for ring1 in attack_rings:
        for ring2 in attack_rings:            
            if ring1 != ring2:
                attack_options.append(attack_inventory_option(weapon, ring1, ring2))
            if ring1 is None and ring2 is None:
                attack_options.append(attack_inventory_option(weapon, None, None))

defend_options = []
for armor in armors:
    for ring1 in armor_rings:
        for ring2 in armor_rings:
            if ring1 != ring2:
                defend_options.append(defend_inventory_option(armor, ring1, ring2))
            if ring1 is None and ring2 is None:
                defend_options.append(defend_inventory_option(armor, None, None))


class full_equipment_option():

    def __init__(self, attack: attack_inventory_option, defend: defend_inventory_option):
        self.attack = attack
        self.defend = defend

        self.total_cost = attack.total_cost + defend.total_cost
        self.total_damage = attack.total_damage
        self.total_armour = defend.total_armour

        rounds_till_death = my_hit_points / (boss_damage - self.total_armour) if boss_damage - self.total_armour > 0 else my_hit_points
        rounds_till_boss_death = boss_hit_points / (self.total_damage - boss_armour) if self.total_damage - boss_armour > 0 else boss_hit_points

        self.i_win = rounds_till_boss_death <= rounds_till_death

        if self.attack.tworings and self.defend.tworings:
            self.i_win = False

win_full_equipment_options = []

for attack in attack_options:
    for defend in defend_options:
        option = full_equipment_option(attack, defend)
        if option.i_win:
            win_full_equipment_options.append(option)


win_full_equipment_options.sort(key=lambda x: x.total_cost)

print(win_full_equipment_options[0].total_cost)
