from collections import deque
from fighter import Fighter
from spell import Spell, Spell_Type
from match_state import MatchState
import copy

class Result:
    PLAYER_WIN = "Player Win"
    BOSS_WIN = "Boss Win"
    ONGOING = "Ongoing"
    ERROR = "Error"

# count the result for one spell sequence, however this seeemsto be a dead end.
class match_counter():
    def __init__(self,
                 player_spells:list,
                 player:Fighter,
                 boss:Fighter,
        ):
        
        self.count = 0
        self.all_player_spells = player_spells

        self.player = player
        self.boss = boss

        self.remianing_player_spells = deque(player_spells)

        self.player_active_spells: list[Spell] = []
        self.result = None
        self.latest_turn = 0
        self.player_mana_spent = 0

    def count_match(self):
        max_turn = 50

        for turn in range(0, max_turn):
            self.latest_turn = turn
            self.player.extra_armor = 0

            for spell in self.player_active_spells:
                spell.lasts -= 1
                if spell.lasts == 0:
                    self.player_active_spells.remove(spell)
                    continue

                if spell.damage:
                    self.boss.hit_points -= spell.damage
                if spell.mana_increase:
                    self.player.mana += spell.mana_increase
                if spell.armor_increase:
                    self.player.armor += spell.armor_increase
                if spell.heal:
                    self.player.hit_points += spell.heal
            
            if self.boss.hit_points <= 0:
                self.result = Result.PLAYER_WIN
                return

            if turn % 2 == 0:
                # Player turn
                if len(self.remianing_player_spells) == 0:
                    self.result = Result.ONGOING
                    return
                spell = self.remianing_player_spells.popleft()
                # check if any spell has the same type in active spells
                if any(s.spell_type == spell.spell_type for s in self.player_active_spells):
                    self.result = Result.ERROR
                    return

                if spell.cost > self.player.mana:
                    self.result = Result.BOSS_WIN
                    return
                self.player.mana -= spell.cost
                self.player_mana_spent += spell.cost
                if spell.effects_instantly:
                    if spell.damage:
                        self.boss.hit_points -= spell.damage
                    if spell.heal:
                        self.player.hit_points += spell.heal
                    if spell.armor_increase:
                        self.player.armor += spell.armor_increase
                else:
                    self.player_active_spells.append(spell)
            
                if self.boss.hit_points <= 0:
                    self.result = Result.PLAYER_WIN
                    return

            else:
                #now its the boss turn
                damage = self.boss.damage - (self.player.armor + self.player.extra_armor)
                if damage < 1:
                    damage = 1
                self.player.hit_points -= damage
                if self.player.hit_points <= 0:
                    self.result = Result.BOSS_WIN
                    return

        self.result = Result.ONGOING
        return


mana_used = int

# A function to cont two turn, counting from the player turn, from a given point.        
def do_one_adok_kapok(start_state: MatchState, next_spell: Spell) -> tuple[Result, MatchState]:

    current_state = copy.copy(start_state)
    current_state.previous_spells = [copy.copy(spell) for spell in start_state.previous_spells]

    if any(spell.spell_type == next_spell.spell_type for spell in current_state.active_spells):
        return Result.ERROR, current_state
    if next_spell.cost > current_state.player_mana:
        return Result.ERROR, current_state

    current_state.player_mana -= next_spell.cost
    current_state.previous_spells.append(next_spell)

    # deal with instant spells
    if next_spell.spell_type == Spell_Type.MAGIC_MISSILE:
        if current_state.boss_hp <= next_spell.damage:
            return Result.PLAYER_WIN, current_state
        current_state.boss_hp -= next_spell.damage

    if next_spell.spell_type == Spell_Type.DRAIN:
        if current_state.boss_hp <= next_spell.damage:
            return Result.PLAYER_WIN, current_state
        current_state.boss_hp -= next_spell.damage
        current_state.player_hp += next_spell.heal

    if next_spell.spell_type in (Spell_Type.SHIELD, Spell_Type.POISON, Spell_Type.RECHARGE):
        current_state.active_spells = [copy.copy(spell) for spell in current_state.active_spells]
        current_state.active_spells.append(copy.copy(next_spell))
    else:
        current_state.active_spells = [copy.copy(spell) for spell in current_state.active_spells]

    player_armor = 0
    spells_to_remove = []

    # player turn
    for spell in current_state.active_spells:
        spell.lasts -= 1
        if spell.spell_type == Spell_Type.SHIELD:
            player_armor = spell.armor_increase
        elif spell.spell_type == Spell_Type.POISON:
            current_state.boss_hp -= spell.damage
        elif spell.spell_type == Spell_Type.RECHARGE:
            current_state.player_mana += spell.mana_increase
        if spell.lasts <= 0:
            spells_to_remove.append(spell)

    for spell in spells_to_remove:
        current_state.active_spells.remove(spell)
    
    spells_to_remove = []

    if current_state.boss_hp <= 0:
        return Result.PLAYER_WIN, current_state

    #boss turn
    current_state.player_hp -= max(1, current_state.boss_damage - player_armor)

    if current_state.player_hp <= 0:
        return Result.BOSS_WIN,current_state

    for spell in current_state.active_spells:
        spell.lasts -= 1
        if spell.spell_type == Spell_Type.SHIELD:
            player_armor = spell.armor_increase
        elif spell.spell_type == Spell_Type.POISON:
            current_state.boss_hp -= spell.damage
        elif spell.spell_type == Spell_Type.RECHARGE:
            current_state.player_mana += spell.mana_increase
        if spell.lasts <= 0:
            spells_to_remove.append(spell)

    for spell in spells_to_remove:
        current_state.active_spells.remove(spell)

    if current_state.boss_hp <= 0:
        return Result.PLAYER_WIN, current_state

    return Result.ONGOING, current_state
