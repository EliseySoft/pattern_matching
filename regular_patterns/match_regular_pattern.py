from enum import Enum
from typing import Any

from regular_patterns.kmp import kmp
from utils import VARIABLES


def parse_regular_pattern(regular_pattern: str) -> list[str]:
    blocks = []
    chars = regular_pattern.split('_')
    curr_block = ''

    for char in chars:
        if char in VARIABLES:
            if curr_block != '':
                blocks.append(curr_block)
                curr_block = ''
            blocks.append(char)
        else:
            curr_block += char
    if curr_block != '':
        blocks.append(curr_block)
    return blocks


class BlockType(Enum):
    variable: str = 'variable'
    terminals: str = 'terminals'


def get_block_type(block: str) -> BlockType:
    if block in VARIABLES:
        return BlockType.variable
    else:
        return BlockType.terminals


def process_variables(s: str, unprocessed_vars: list[str]):
    d = {}
    # assert len(s) >= len(unprocessed_vars)

    # если переменных больше, чем букв в строке, то мы присваиваем лишним переменным пустые значения
    shift = max(0, len(unprocessed_vars) - len(s))
    for i in range(shift):
        d[unprocessed_vars[i]] = ''

    for i in range(len(s)):
        if i == len(unprocessed_vars) - 1:
            d[unprocessed_vars[i + shift]] = s[i:]
            break
        d[unprocessed_vars[i + shift]] = s[i]
    return d


def match_regular_pattern(s: str, pattern: str) -> dict[str, str]:
    blocks = parse_regular_pattern(regular_pattern=pattern)
    word_pointer = 0
    d = {}  # словарь, в котором будут лежать мэтчи переменных на подстроки
    number_of_unprocessed_variables: int = 0
    unprocessed_vars = []

    start_block = blocks[0]  # первый блок
    finish_block = blocks[-1]  # последний блок

    if get_block_type(start_block) == BlockType.terminals:  # убираем первый блок
        if start_block == s[:len(start_block)]:
            s = s[len(start_block):]
            blocks = blocks[1:]
        else:
            return {}
    if get_block_type(finish_block) == BlockType.terminals:  # убираем последний блок
        if finish_block == s[len(s) - len(finish_block):]:
            s = s[:len(s) - len(finish_block)]
            blocks = blocks[:-1]
        else:
            return {}

    for block in blocks:
        block_type = get_block_type(block)

        if block_type == BlockType.variable:
            # word_pointer += 1  # закомментировал для случаев, когда переменная может быть пустой
            number_of_unprocessed_variables += 1
            unprocessed_vars.append(block)
        else:
            start = kmp(s=block, t=s[word_pointer:]) + word_pointer
            finish = start + len(block)

            if start == word_pointer - 1:  # когда подстрока не нашлась с помощью КМП
                return {}

            substring_for_variables = s[word_pointer:start]
            processed_variables = process_variables(s=substring_for_variables, unprocessed_vars=unprocessed_vars)
            d.update(processed_variables)
            number_of_unprocessed_variables = 0
            unprocessed_vars = []

            word_pointer = finish

    if len(unprocessed_vars) > 0:
        substring_for_variables = s[word_pointer:]
        processed_variables = process_variables(s=substring_for_variables, unprocessed_vars=unprocessed_vars)
        d.update(processed_variables)
    return d
