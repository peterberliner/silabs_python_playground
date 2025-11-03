from match_state import MatchState
from typing import Tuple
from match_counter import Result, do_one_adok_kapok
from spell import Spell, Spell_Type


def run_one_branch_one_level(start_state: MatchState) -> Tuple[list[MatchState], list[MatchState]]:
    ongoing = []
    wins = []
    for next_spell in [
        Spell(Spell_Type.MAGIC_MISSILE),
        Spell(Spell_Type.DRAIN),
        Spell(Spell_Type.SHIELD),
        Spell(Spell_Type.POISON),
        Spell(Spell_Type.RECHARGE),
        ]:
        result, new_state = do_one_adok_kapok(start_state, next_spell)
        if result == Result.ONGOING:
            ongoing.append(new_state)
        elif result == Result.PLAYER_WIN:
            wins.append(new_state)

    return ongoing, wins

def check_all() -> list[MatchState]:
    start_state = MatchState(
        previous_spells=[],
        active_spells=[],
        boss_hp=71,
        boss_damage=10,
        player_hp=50,
        player_mana=500,
    )
    active_matches = [start_state]
    wins = []

    while active_matches:
        ongoing = []
        for match in active_matches:
            ongoing_results, wins_results = run_one_branch_one_level(match)
            wins.extend(wins_results)
            ongoing.extend(ongoing_results)
        active_matches = ongoing
        print(f"Active matches: {len(active_matches)}, Wins so far: {len(wins)}")

    return wins

class sumsum:
    sum_counter = 0

def count_mana_used(state: MatchState) -> int:
    sumsum.sum_counter += 1
    mana_cost = 0
    for spell in state.previous_spells:
        mana_cost += spell.cost
    # mana_cost = sum(spell.cost for spell in state.previous_spells)
    print(f"Counting mana for state {sumsum.sum_counter}. mana cost: {mana_cost}")
    return mana_cost

def get_min_mana_used(states: list[MatchState]) -> int:
    return min(count_mana_used(state) for state in states)

if __name__ == "__main__":

    print("------------------------------")

    wins = check_all()
    print(f"Total wins: {len(wins)}")

    if wins:
       min_mana = get_min_mana_used(wins)
       print(f"Minimum mana used to win: {min_mana}")
