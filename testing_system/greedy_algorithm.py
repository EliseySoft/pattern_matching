from collections import deque
from dataclasses import dataclass
from typing import Optional

from utils import VARIABLES


@dataclass
class IterData:
    w: str  # строка
    p: str  # шаблон (в нём меняем переменные на терминалы во время цикла)
    variables: list[str]
    matched_variables: dict[str, str]


def find_variants(w: str) -> list[str]:
    """Функция, которая ищет все варианты префиксов строки, включая пустую строку и всю строку"""

    variants = [w[:i] for i in range(len(w) + 1)]
    return variants


def substitute_variables(p: str, var: str, substitution: str):
    """Функция, которая заменяет переменную в шаблоне на строку и возвращает получившийся шаблон"""

    new_w = ''
    chars = p.split('_')
    substitution = '_'.join(list(substitution))
    for char in chars:
        if char == var:  # нужная переменная
            new_w += f'_{substitution}' if (len(new_w) != 0 and substitution != '') else substitution
        else:  # терминал или остальные переменные
            new_w += f'_{char}' if len(new_w) != 0 else char

    return new_w


def can_match(w: str, p: str, var_char: str) -> bool:
    """Функция, которая принимает шаблон и строку и проверяет,
    совпадают ли терминалы в шаблоне до первой не смэтченной переменной с соответствующими символами из строки.
    Если поймали какое-то несовпадение, то возвращаем `False`, иначе возвращаем `True`
    """

    pattern_chars = p.split('_')

    for i in range(len(pattern_chars)):
        if pattern_chars[i] == var_char:
            break
        elif i >= len(w):
            return False
        elif pattern_chars[i] == w[i]:
            continue
        else:
            return False

    return True


def find_variables(p: str) -> list[str]:
    """Функция возвращает список переменных в том порядке, в котором они встречаются в шаблоне"""

    variables = []
    seen_variables = set()
    chars = p.split('_')

    for char in chars:
        if char in VARIABLES and char not in seen_variables:
            variables.append(char)
            seen_variables.add(char)
        else:
            continue
    return variables


def greedy_matching_algorithm(s: str, pattern: str) -> Optional[dict[str, str]]:
    variables = find_variables(p=pattern)

    q = deque()
    q.append(IterData(w=s, p=pattern, variables=variables, matched_variables={}))

    while len(q) > 0:
        data: IterData = q.pop()  # Достаем текущую ветвь дерева из очереди

        if len(data.matched_variables) == len(data.variables):
            # print(f'word: {data.w}')
            # print(f'pattern: {"".join(data.p.split("_"))}', end='\n\n')
            if ''.join(data.p.split('_')) == data.w:
                return data.matched_variables
            else:
                continue

        # Первая переменная по порядку в строке еще не смэтченная
        current_variable: str = data.variables[len(data.matched_variables)]

        start_from = data.p.split('_').index(
            current_variable)  # откуда в строке начинаем искать соответствия для переменной

        # проверка, что совпадает начало
        start_is_invalid = False
        pattern_chars = data.p.split('_')
        for i in range(start_from):
            if pattern_chars[i] == data.w[i]:
                continue
            else:
                start_is_invalid = True
                break

        if start_is_invalid:
            continue

        variants = find_variants(data.w[start_from:])  # находим варианты значений для переменной (с пустой строкой)

        for variant in variants:
            # заменяем переменную в шаблоне только что найденными вариантами
            new_pattern = substitute_variables(p=data.p, var=current_variable, substitution=variant)

            if current_variable == data.variables[-1]:
                next_variable = None
            else:
                # берём следующую не смэтченную переменную
                next_variable = data.variables[len(data.matched_variables) + 1]

            if not can_match(w=data.w, p=new_pattern, var_char=next_variable):
                # Определяем, не противоречит ли текущий метчинг переменных исходной строке
                # Итерируемся по шаблону и строке, пока не найдём первую переменную, для которой значение ещё не подбирали
                # Если при проходе на i позиции терминал из строки не совпадает с терминалом из шаблона, то возвращаем False
                continue

            q.append(
                IterData(
                    w=data.w,
                    p=new_pattern,
                    variables=data.variables,
                    matched_variables=data.matched_variables | {current_variable: variant}
                )
            )

    return {}
