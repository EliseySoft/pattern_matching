from itertools import permutations
from typing import Tuple, List, Any


def permutations_has_intersections(perm1: tuple[int, ...], perm2: tuple[int, ...]) -> bool:
    has_intersections = False
    for i in range(len(perm1)):
        start1 = min(perm1[i], perm2[i])  # фиксируем начало у первой перестановки
        end1 = max(perm1[i], perm2[i])  # фиксируем конец у первой перестановки

        if start1 == -1 or end1 == -1:
            continue

        for j in range(i + 1, len(perm1)):
            start2 = min(perm1[j], perm2[j])  # фиксируем начало у второй перестановки
            end2 = max(perm1[j], perm2[j])  # фиксируем конец у второй перестановки

            if start2 == -1 or end2 == -1:
                continue

            if start1 <= start2 <= end1 or start2 <= start1 <= end2:
                has_intersections = True
                return has_intersections

    return has_intersections


def create_permutations(n: int, k: int) -> tuple[list[Any], list[Any]]:
    numbers = list(range(n))
    for _ in range(k):  # для пустых строк, но это замедляет алгоритм
        numbers.append(-1)
    first_set = list(permutations(numbers, k))

    final_first_set = []
    final_second_set = []

    for i in range(len(first_set)):
        first_set_values = set(first_set[i])
        second_set_values = list(set(list(range(n))).difference(first_set_values))
        second_set = list(permutations(second_set_values, k))

        for j in range(len(second_set)):

            if not permutations_has_intersections(first_set[i], second_set[j]):  # убираем лишние перестановки
                final_first_set.append(first_set[i])
                final_second_set.append(second_set[j])

    return final_first_set, final_second_set
