from itertools import combinations
from collections.abc import Iterator
from math import prod

candidate_groups = [(list[int],list[int])]

presents = []
presents_modulo_2 = []
presents_modulo_3 = []
presents_modulo_5 = []
presents_modulo_7 = []
presents_modulo_41 = []


def check_one_combination(present_indexes = list[int], target_weight = int) -> bool:
    if sum(presents_modulo_2[present_index] for present_index in present_indexes) % 2 != target_weight % 2:
        return False
    if sum(presents_modulo_3[present_index] for present_index in present_indexes) % 3 != target_weight % 3:
        return False
    if sum(presents_modulo_5[present_index] for present_index in present_indexes) % 5 != target_weight % 5:
        return False
    if sum(presents_modulo_7[present_index] for present_index in present_indexes) % 7 != target_weight % 7:
        return False
    if sum(presents_modulo_41[present_index] for present_index in present_indexes) % 41 != target_weight % 41:
        return False
    if sum(presents[present_index] for present_index in present_indexes) == target_weight:
        return True
    return False

def check_all_combination(present_indexes_combination = list[int], target_weight = int) -> list[list[int]] | None:
    result = []
    for present_indexes in present_indexes_combination:
        if check_one_combination(present_indexes, target_weight):
            result.append(present_indexes)
    return result

def check_all_combination_stop_first(present_indexes_combination = list[int], target_weight = int) -> bool:
    for present_indexes in present_indexes_combination:
        if check_one_combination(present_indexes, target_weight):
            return True
    else:
        return False


if __name__ == "__main__":
    with open(r"AdventOfCode\2015\Day24\input.txt") as f:
        lines = f.read().splitlines()

    presents = [int(line) for line in lines]
    all_present_weight = sum(presents)
    third_weight = all_present_weight // 3

    presents_modulo_2 = [p % 2 for p in presents]
    presents_modulo_3 = [p % 3 for p in presents]
    presents_modulo_5 = [p % 5 for p in presents]
    presents_modulo_7 = [p % 7 for p in presents]
    presents_modulo_41 = [p % 41 for p in presents]

    candidate_groups = []

    for i in range(10):
        candidates = combinations(range(len(lines)), i)
        new_candidate_groups = check_all_combination(candidates, third_weight)
        if new_candidate_groups:
            candidate_groups.extend(new_candidate_groups)
        print(f"Checked combinations of size {i}, found {len(candidate_groups)} valid groups so far.")

    valid_candidate_groups = []

    min_len = 10
    min_qe = prod(presents)


    for candidate_group in candidate_groups:
        if len(candidate_group) > min_len:
            continue
        if len(candidate_group) < min_len:
            min_len = len(candidate_group)

        remaining_present_indexes = [i for i in range(len(lines)) if i not in candidate_group]
        for i in range(10):
            candidates = combinations(remaining_present_indexes, i)
            if check_all_combination_stop_first(candidates, third_weight):
                qe = prod([presents[i] for i in candidate_group])
                #tricky here...
                if qe < min_qe:
                    min_qe = qe
                print(f"Found one! len: {len(candidate_group)}. qe: {qe}")                
                valid_candidate_groups.append(candidate_group)
                print(f"Found {len(valid_candidate_groups)} valid groups so far.")

                print(candidate_group)
                continue


    print(f"All done. Min len = {min_len}. min_qe: {min_qe}")
    for valid_candidate_group in valid_candidate_groups:
        print(valid_candidate_group)
