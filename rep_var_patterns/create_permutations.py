from itertools import permutations
from typing import Tuple, List, Any


def permutations_has_intersections(perm1: tuple[int, ...], perm2: tuple[int, ...]) -> bool:
    has_intersections = False
    for i in range(len(perm1)):
        start1 = min(perm1[i], perm2[i])  # фиксируем начало у первой перестановки
        end1 = max(perm1[i], perm2[i])  # фиксируем конец у первой перестановки

        for j in range(i + 1, len(perm1)):
            start2 = min(perm1[j], perm2[j])  # фиксируем начало у второй перестановки
            end2 = max(perm1[j], perm2[j])  # фиксируем конец у второй перестановки

            if start1 <= start2 <= end1 or start2 <= start1 <= end2:
                has_intersections = True
                return has_intersections

    return has_intersections


def create_permutations(n: int, k: int) -> tuple[list[Any], list[Any]]:
    numbers = list(range(n))
    first_set = list(permutations(numbers, k))
    second_set = list(permutations(numbers, k))

    first_set_without_intersections = []
    second_set_without_intersections = []

    for i in range(len(first_set)):
        for j in range(len(second_set)):
            # perm1 = set(first_set[i])
            # perm2 = set(second_set[j])
            #
            # # if len(perm1.intersection(perm2)) == 0:
            if not permutations_has_intersections(first_set[i], second_set[j]):
                first_set_without_intersections.append(first_set[i])
                second_set_without_intersections.append(second_set[j])

    # final_first_set = []
    # final_second_set = []
    #
    # # проверка, что перестановка не залазит в границы другой перестановки
    #
    # for i in range(len(first_set_without_intersections)):
    #     perm1 = first_set_without_intersections[i]
    #     perm2 = second_set_without_intersections[i]
    #
    #     has_intersections = permutations_has_intersections(perm1, perm2)
    #
    #     if has_intersections:
    #         continue
    #     else:
    #         final_first_set.append(perm1)
    #         final_second_set.append(perm2)

    return first_set_without_intersections, second_set_without_intersections


# if __name__ == "__main__":
#     n = 6
#     k = 2
#     first_set, second_set = create_permutations(n, k)
#     print(first_set)
#     print(second_set)
