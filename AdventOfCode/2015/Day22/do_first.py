from match_counter import match_counter
from fighter import Fighter
from spell import Spell, Spell_Type
from itertools import product
import math

def run_example_one():
    player_spells_example1 = [
        Spell(Spell_Type.POISON),
        Spell(Spell_Type.MAGIC_MISSILE),
    ]

    player_example_1 = Fighter("Player", hit_points=10, mana=250)
    boss_example_1 = Fighter("Boss", hit_points=13, damage=8)

    mc = match_counter(
        player_spells=player_spells_example1,
        player=player_example_1,
        boss=boss_example_1,
    )



    mc.count_match()

    print(f"Match result: {mc.result}")
    print(f"Match turn_count: {mc.latest_turn}")
    print(f"Match player_mana_spent: {mc.player_mana_spent}")


def run_example_two():
    player_spells_example1 = [
        Spell(Spell_Type.RECHARGE),
        Spell(Spell_Type.SHIELD),
        Spell(Spell_Type.DRAIN),
        Spell(Spell_Type.POISON),
        Spell(Spell_Type.MAGIC_MISSILE),
    ]

    player_example_1 = Fighter("Player", hit_points=10, mana=250)
    boss_example_1 = Fighter("Boss", hit_points=14, damage=8)

    mc = match_counter(
        player_spells=player_spells_example1,
        player=player_example_1,
        boss=boss_example_1,
    )

    mc.count_match()

    print(f"Match result: {mc.result}")
    print(f"Match turn_count: {mc.latest_turn}")
    print(f"Match player_mana_spent: {mc.player_mana_spent}")


if __name__ == "__main__":
    run_example_one()
    run_example_two()

    available_spells = [
        Spell(Spell_Type.MAGIC_MISSILE),
        Spell(Spell_Type.DRAIN),
        Spell(Spell_Type.SHIELD),
        Spell(Spell_Type.POISON),
        Spell(Spell_Type.RECHARGE),
        ]

    spell_combinations = product(available_spells, repeat=12  )

    boss_wins = 0
    ongoing = 0
    player_wins = 0
    errors_count = 0
    min_mana_spent = math.inf

    print("------------------------------")

    print(f"Total combinations to evaluate: {len(spell_combinations)}")

    for combination in spell_combinations:
        copied_combination = [Spell(spell.spell_type) for spell in combination]
        player = Fighter("Player", hit_points=50, mana=500)
        boss = Fighter("Boss", hit_points=71, damage=10)

        mc = match_counter(
            player_spells=list(copied_combination),
            player=player,
            boss=boss,
        )

        mc.count_match()

        if mc.result == "Player Win":
            print(f"Match result: {mc.result}")
            print(f"Match turn_count: {mc.latest_turn}")
            print(f"Match player_mana_spent: {mc.player_mana_spent}")
            if mc.player_mana_spent < min_mana_spent:
                min_mana_spent = mc.player_mana_spent
                print(f"New minimum mana spent found: {min_mana_spent}")

        if mc.result == "Boss Win":
            boss_wins += 1
        elif mc.result == "Ongoing":
            ongoing += 1
        elif mc.result == "Player Win":
            player_wins += 1
        elif mc.result == "Error":
            errors_count += 1

    print(f"Boss wins: {boss_wins}")
    print(f"Ongoing: {ongoing}")
    print(f"Player wins: {player_wins}")
    print(f"Errors: {errors_count}")
    print(f"Minimum mana spent for a win: {min_mana_spent}")

