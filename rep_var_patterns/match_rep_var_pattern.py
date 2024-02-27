from rep_var_patterns.create_permutations import create_permutations
from one_rep_var_patterns.match_one_rep_var_pattern import match_one_rep_var_pattern
from one_var_patterns.match_one_var_pattern import match_one_var_pattern
from utils import VARIABLES, check_pattern


def find_first_rep_var(pattern: str) -> str:
    """Функция, которая возвращает первую встретившуюся переменную"""
    d = {}
    variables = []

    for char in pattern.split('_'):
        if char not in VARIABLES:
            continue

        d[char] = d.get(char, 0) + 1
        variables.append(char)

    for char in variables:
        if d[char] > 1:
            return char


def find_rep_vars(pattern: str, first_rep_var: str) -> list[str]:
    """Функция, которая возвращает список повторяющихся переменных без первой повторяющейся переменной"""
    rep_vars = []
    d = {}
    for char in pattern.split('_'):
        if char not in VARIABLES or char == first_rep_var:
            continue
        d[char] = d.get(char, 0) + 1

    for char in d:
        if d[char] > 1:
            rep_vars.append(char)

    return rep_vars


def match_rep_var_pattern(s: str, pattern: str) -> dict[str, str]:
    first_rep_var = find_first_rep_var(pattern)
    rep_vars = find_rep_vars(pattern, first_rep_var=first_rep_var)
    start_perms, end_perms = create_permutations(n=len(s), k=len(rep_vars))

    for i in range(len(start_perms)):
        rep_vars_images = {}
        start_perm = start_perms[i]
        end_perm = end_perms[i]

        for j in range(len(start_perm)):
            var = rep_vars[j]
            start = min(start_perm[j], end_perm[j])
            end = max(start_perm[j], end_perm[j])
            rep_vars_images[var] = s[start:end+1]

        new_pattern = '_'.join(rep_vars_images[char] if char in rep_vars_images else char for char in pattern.split('_'))  # получили one_rep_var_patterns
        num_of_vars = sum(1 for char in set(new_pattern.split('_')) if char in VARIABLES)

        if num_of_vars == 1:
            result, matches = match_one_var_pattern(s=s, pattern=new_pattern, var_char=first_rep_var)

            if result:
                rep_vars_images.update(matches)
                return rep_vars_images
            # else:
            #     return {}
        else:
            matches = match_one_rep_var_pattern(s=s, pattern=new_pattern)

            if len(matches) == 0:
                continue
            else:
                rep_vars_images.update(matches)
                return rep_vars_images
    return {}
