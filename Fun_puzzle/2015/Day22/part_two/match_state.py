from spell import Spell

# Have one stat, where the previous used spells, the currenlty active spells, boss hit points, player hit points and player mana are stored
class MatchState:
    def __init__(self, 
                 previous_spells: list[Spell], 
                 active_spells: list[Spell], 
                 boss_hp: int, 
                 player_hp: int, 
                 player_mana: int, 
                 boss_damage: int):
        self.previous_spells = previous_spells  # List of spells used in order
        self.active_spells = active_spells      # List of currently active spells
        self.boss_hp = boss_hp                  # Current hit points of the boss
        self.player_hp = player_hp              # Current hit points of the player
        self.player_mana = player_mana          # Current mana of the player
        self.boss_damage = boss_damage          # Current damage of the boss
