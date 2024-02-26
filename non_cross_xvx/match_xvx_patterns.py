from utils import ALPHABET, VARIABLES


def z_function(s, v_substring: str):
    """Модифицированная z-функция, которая ищет повторения вида xvx"""

    n = len(s)
    z = [0] * n
    l, r = 0, 0
    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l = i
            r = i + z[i] - 1

    for i in range(len(z)):
        if z[i] == 0:
            continue
        if s[i - len(v_substring):i] == v_substring and i > len(v_substring):
            if z[i] > i:
                z[i] = i
            if z[i] == i:
                z[i] -= len(v_substring)
                continue
            elif z[i] + len(v_substring) == i:
                continue
            elif z[i] + len(v_substring) > i:
                z[i] = i - len(v_substring)
            else:
                z[i] = 0

        else:
            z[i] = 0
    return z


def construct_repetitions(z: list[int]) -> list[tuple[int, int]]:
    reps = [(-1, -1)]
    for i in range(len(z)):
        if z[i] == 0:
            continue
        start = 0
        finish = i + z[i] - 1

        reps.append((start, finish))
    reps = [rep for rep in reps if (rep[0] == 0 or rep[0] == -1)]  # для пустой переменной rep[0] == -1
    return reps


def find_xvx_repetitions(s: str, v_substring: str):
    """Возвращает список индексов подстроки, который соответствуют множителям шаблона вида xvx"""
    z = z_function(s, v_substring)
    reps = construct_repetitions(z)
    return reps


def match_xvx_block_with_str(s: str, block: str, v_substring: str, repetition: tuple[int, int]) -> tuple[bool, str | None, str, str]:
    """
    Функция, которая пытается смэтчить строку с блоком.
    Если удалось, то возвращает результат, новую строку, мэтч для переменной и символ переменной.
    """
    block_chars = block.split('_')  # все терминалы и переменные в блоке
    variable = block_chars[0]  # переменная
    if repetition[0] == -1 and repetition[1] == -1:
        variable_match_len = 0
        variable_match = ''
    else:
        variable_match_len = (repetition[1] + 1 - len(v_substring)) // 2
        variable_match = s[0: variable_match_len]

    word_pointer = 0

    for char in block_chars:
        if char in ALPHABET:
            if char == s[word_pointer]:
                word_pointer += 1
            else:
                return False, '', variable, variable_match
        else:
            if s[word_pointer:word_pointer + variable_match_len] == variable_match:
                word_pointer += len(variable_match)
            else:
                return False, '', variable, variable_match
        if word_pointer > len(s):
            return False, '', variable, variable_match
    return True, s[word_pointer:], variable, variable_match
