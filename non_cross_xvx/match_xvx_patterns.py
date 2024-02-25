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
    reps = []
    for i in range(len(z)):
        if z[i] == 0:
            continue
        start = 0
        finish = i + z[i] - 1

        reps.append((start, finish))
    reps = [rep for rep in reps if rep[0] == 0]
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
            word_pointer += len(variable_match)
        if word_pointer > len(s):
            return False, '', variable, variable_match
    return True, s[word_pointer:], variable, variable_match


def test():
    s = 'baaabadfgh'
    v_substring = 'aa'
    repetitions = find_xvx_repetitions(s, v_substring)
    assert repetitions == [(0, 5)]
    print(f'word = {s}, v = {v_substring}')
    for rep in repetitions:
        print(s[rep[0]: rep[1] + 1], rep)
    print()

    s = 'abcdabcabc'
    v_substring = 'd'
    repetitions = find_xvx_repetitions(s, v_substring)
    assert repetitions == [(0, 6)]
    print(f'word = {s}, v = {v_substring}')
    for rep in repetitions:
        print(s[rep[0]: rep[1] + 1], rep)
    print()

    s = 'kjjjjjk'
    v_substring = 'jjjjj'
    repetitions = find_xvx_repetitions(s, v_substring)
    assert repetitions == [(0, 6)]
    print(f'word = {s}, v = {v_substring}')
    for rep in repetitions:
        print(s[rep[0]: rep[1] + 1], rep)
    print()

    s = 'klmjjjjjklm'
    v_substring = 'jjjjj'
    repetitions = find_xvx_repetitions(s, v_substring)
    assert repetitions == [(0, 10)]
    print(f'word = {s}, v = {v_substring}')
    for rep in repetitions:
        print(s[rep[0]: rep[1] + 1], rep)
    print()

    s = 'abcdeabc'
    v_substring = 'e'
    repetitions = find_xvx_repetitions(s, v_substring)
    assert repetitions == []
    print(f'word = {s}, v = {v_substring}')
    for rep in repetitions:
        print(s[rep[0]: rep[1] + 1], rep)
    print()

    s = 'abckpbababc'
    v_substring = 'kpbab'
    repetitions = find_xvx_repetitions(s, v_substring)
    assert repetitions == [(0, 10)]
    print(f'word = {s}, v = {v_substring}')
    for rep in repetitions:
        print(s[rep[0]: rep[1] + 1], rep)
    print()

    s = 'addddabadddd'
    v_substring = 'dab'
    repetitions = find_xvx_repetitions(s, v_substring)
    assert repetitions == [(0, 10)]
    print(f'word = {s}, v = {v_substring}')
    for rep in repetitions:
        print(s[rep[0]: rep[1] + 1], rep)
    print()

    s = 'aaaaaaaaaaaddsjkadfhweqjopdlmxwkqn'
    v_substring = 'aa'
    repetitions = find_xvx_repetitions(s, v_substring)
    assert repetitions == [(0, 3), (0, 5), (0, 7), (0, 9)]
    print(f'word = {s}, v = {v_substring}')
    for rep in repetitions:
        print(s[rep[0]: rep[1] + 1], rep)
    print()

    s = 'abcdertyuiiopljgggggfa'
    v_substring = 'bcdertyuiiopljgggggf'
    repetitions = find_xvx_repetitions(s, v_substring)
    assert repetitions == [(0, 21)]
    print(f'word = {s}, v = {v_substring}')
    for rep in repetitions:
        print(s[rep[0]: rep[1] + 1], rep)
    print()

    s = 'aaaaa'
    v_substring = 'a'
    repetitions = find_xvx_repetitions(s, v_substring)
    assert repetitions == [(0, 2), (0, 4)]
    print(f'word = {s}, v = {v_substring}')
    for rep in repetitions:
        print(s[rep[0]: rep[1] + 1], rep)
    print()

    s = 'aaaaaa'
    v_substring = 'a'
    repetitions = find_xvx_repetitions(s, v_substring)
    assert repetitions == [(0, 2), (0, 4)]
    print(f'word = {s}, v = {v_substring}')
    for rep in repetitions:
        print(s[rep[0]: rep[1] + 1], rep)
    print()

    s = 'abcabc'
    v_substring = 'c'
    repetitions = find_xvx_repetitions(s, v_substring)
    assert repetitions == [(0, 4)]
    print(f'word = {s}, v = {v_substring}')
    for rep in repetitions:
        print(s[rep[0]: rep[1] + 1], rep)
    print()

    s = 'abababab'
    v_substring = 'ab'
    repetitions = find_xvx_repetitions(s, v_substring)
    assert repetitions == [(0, 5)]
    print(f'word = {s}, v = {v_substring}')
    for rep in repetitions:
        print(s[rep[0]: rep[1] + 1], rep)
    print()

    s = 'baaabaaaa'
    v_substring = 'aa'
    repetitions = find_xvx_repetitions(s, v_substring)
    assert repetitions == [(0, 5)]
    print(f'word = {s}, v = {v_substring}')
    for rep in repetitions:
        print(s[rep[0]: rep[1] + 1], rep)
    print()

    s = 'aaaaaapoiu'
    v_substring = 'aa'
    repetitions = find_xvx_repetitions(s, v_substring)
    assert repetitions == [(0, 3), (0, 5)]
    print(f'word = {s}, v = {v_substring}')
    for rep in repetitions:
        print(s[rep[0]: rep[1] + 1], rep)
    print()

    s = 'aababaab'
    v_substring = 'ab'
    repetitions = find_xvx_repetitions(s, v_substring)
    assert repetitions == [(0, 3), (0, 7)]
    print(f'word = {s}, v = {v_substring}')
    for rep in repetitions:
        print(s[rep[0]: rep[1] + 1], rep)
    print()

    s = 'acbdfghacbd'
    v_substring = 'fgh'
    repetitions = find_xvx_repetitions(s, v_substring)
    assert repetitions == [(0, 10)]
    print(f'word = {s}, v = {v_substring}')
    for rep in repetitions:
        print(s[rep[0]: rep[1] + 1], rep)
    print()

    s = 'acbdfghekacbd'
    v_substring = 'fghek'
    repetitions = find_xvx_repetitions(s, v_substring)
    assert repetitions == [(0, 12)]
    print(f'word = {s}, v = {v_substring}')
    for rep in repetitions:
        print(s[rep[0]: rep[1] + 1], rep)
    print()

    s = 'acbdfghekacbdmlkpiunh'
    v_substring = 'fghek'
    repetitions = find_xvx_repetitions(s, v_substring)
    assert repetitions == [(0, 12)]
    print(f'word = {s}, v = {v_substring}')
    for rep in repetitions:
        print(s[rep[0]: rep[1] + 1], rep)
    print()

    s = 'abcdeabcg'
    v_substring = 'de'
    repetitions = find_xvx_repetitions(s, v_substring)
    assert repetitions == [(0, 7)]
    print(f'word = {s}, v = {v_substring}')
    for rep in repetitions:
        print(s[rep[0]: rep[1] + 1], rep)
    print()

    s = 'abcdegabcplkmn'
    v_substring = 'deg'
    repetitions = find_xvx_repetitions(s, v_substring)
    assert repetitions == [(0, 8)]
    print(f'word = {s}, v = {v_substring}')
    for rep in repetitions:
        print(s[rep[0]: rep[1] + 1], rep)
    print()


if __name__ == '__main__':
    test()
