from non_cross_xx.find_repetitions import find_xx_repetitions
from utils import parse_pattern, ALPHABET, VARIABLES


def match_xx_block_with_str(s: str, block: str, repetition: tuple[int, int]) -> tuple[bool, str | None, str, str]:
    """
    Функция, которая мэтчит блок с входной строкой и возвращает суффикс исходной строки.
    :param s: Входная строка
    :param block: Блок с одной переменной, который надо смэтчить к части строки или всей строке.
    :param repetition: Подстрока исходной строки, которая содержит два вхождения переменной из блока.
    :return: Часть исходной, получившаяся удалением соотнесённого блока с началом строки
    """

    block_chars = block.split('_')  # все терминалы и переменные в блоке
    variable = block_chars[0]  # переменная

    # для случая, когда переменная равна пустой
    # if repetition[0] == -1 and repetition[1] == -1:
    #     variable_match = ''
    # else:
    variable_match = s[repetition[0]:repetition[0] + (repetition[1] - repetition[0] + 1) // 2]  # мэтч для переменной

    word_pointer = 0

    for char in block_chars:
        if word_pointer >= len(s):
            return False, '', variable, variable_match

        if char in ALPHABET:
            if char == s[word_pointer]:
                word_pointer += 1
            else:
                return False, '', variable, variable_match
        else:
            if s[word_pointer: word_pointer + len(variable_match)] == variable_match:
                word_pointer += len(variable_match)
            else:
                return False, '', variable, variable_match

    return True, s[word_pointer:], variable, variable_match


def match_xx_patterns(s: str, blocks: list[str], matches: dict[str, str]):
    if len(blocks) == 0:
        return {}

    block = blocks[0]

    # если блок начинается не с переменной
    for i, char in enumerate(block.split('_')):
        if char in VARIABLES:
            break
        if char == s[i]:
            s = s[1:]
            block = '_'.join(block.split('_')[1:])

    repetitions = list(set(find_xx_repetitions(s=s)))
    repetitions = [rep for rep in repetitions if rep[0] == 0]

    for repetition in repetitions:
        flag, new_s, variable, variable_match = match_xx_block_with_str(s, block, repetition=repetition)
        if not flag:  # мэтч не получился
            continue
        matches[variable] = variable_match
        if new_s == '' and flag:  # строка закончилась
            return matches
        match_xx_patterns(s=new_s, blocks=blocks[1:], matches=matches)  # продолжаем мэтчить

    return matches
