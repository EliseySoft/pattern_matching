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
    assert len(s) >= len(unprocessed_vars)

    for i in range(len(s)):
        if i == len(unprocessed_vars) - 1:
            d[unprocessed_vars[i]] = s[i:]
            break
        d[unprocessed_vars[i]] = s[i]
    return d


def match_regular_pattern(word: str, regular_pattern: str) -> tuple[bool, dict[Any, Any]]:
    blocks = parse_regular_pattern(regular_pattern=regular_pattern)
    word_pointer = 0
    d = {}  # словарь, в котором будут лежать мэтчи переменных на подстроки
    number_of_unprocessed_variables: int = 0
    unprocessed_vars = []

    start_block = blocks[0]  # первый блок
    finish_block = blocks[-1]  # последний блок

    if get_block_type(start_block) == BlockType.terminals:  # убираем первый блок
        if start_block == word[:len(start_block)]:
            word = word[len(start_block):]
            blocks = blocks[1:]
        else:
            return False, {}
    if get_block_type(finish_block) == BlockType.terminals:  # убираем последний блок
        if finish_block == word[len(word) - len(finish_block):]:
            word = word[:len(word) - len(finish_block)]
            blocks = blocks[:-1]
        else:
            return False, {}

    for block in blocks:
        block_type = get_block_type(block)

        if block_type == BlockType.variable:
            word_pointer += 1
            number_of_unprocessed_variables += 1
            unprocessed_vars.append(block)
        else:
            start = kmp(s=block, t=word[word_pointer:]) + word_pointer
            finish = start + len(block)

            if start == word_pointer - 1:
                return False, {}

            substring_for_variables = word[word_pointer - number_of_unprocessed_variables:start]
            processed_variables = process_variables(s=substring_for_variables, unprocessed_vars=unprocessed_vars)
            d.update(processed_variables)
            number_of_unprocessed_variables = 0
            unprocessed_vars = []

            word_pointer = finish

    if len(unprocessed_vars) > 0:
        substring_for_variables = word[word_pointer - number_of_unprocessed_variables:]
        processed_variables = process_variables(s=substring_for_variables, unprocessed_vars=unprocessed_vars)
        d.update(processed_variables)
    return True, d


# if __name__ == "__main__":
#     word = 'unajvvnkuratvtxxmgsg'
#     pattern = 'x1_x2_x3_g'
#     # original_matches = {'x1': 'unajvv', 'x2': 'nkuratvtxx', 'x3': 'mgs'}
#
#     result, matches = match_regular_pattern(word=word, regular_pattern=pattern)
#     pattern_is_correct = check_pattern(s=word, pattern=pattern, matches=matches)
#
#     if pattern_is_correct:
#         print("Correct!")
#     else:
#         print("Incorrect!")
#         print(f's: {word}')
#         print(f'p: {pattern}')
#         print(f'matches: {matches}')
