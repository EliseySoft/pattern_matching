from enum import Enum

from non_cross_xx.match_xx_patterns import find_xx_repetitions, match_xx_block_with_str
from non_cross_xvx.match_xvx_patterns import find_xvx_repetitions, match_xvx_block_with_str
from utils import parse_pattern, check_pattern, VARIABLES


class BlockType(Enum):
    """Класс возможных типов блока: xx или xvx."""

    xx_block: str = 'xx'
    xvx_block: str = 'xvx'


def get_block_type(block: str) -> BlockType:
    """Возвращает тип блока (xx или xvx)."""

    chars = block.split('_')

    for i in range(len(chars) - 1):
        if chars[i] == chars[i + 1] and chars[i] in VARIABLES:
            return BlockType.xx_block
        else:
            return BlockType.xvx_block


def find_v_substring(block: str) -> str:
    """Ищет строку v в множители шаблона типа xvx"""

    start = None
    finish = None
    block_chars = block.split('_')

    for i in range(len(block_chars)):
        if block_chars[i] not in VARIABLES:
            continue

        if start is None:
            start = i
        elif finish is None:
            finish = i

    return ''.join(block_chars[start + 1:finish])


def match_non_cross_pattern(s: str, blocks: list[str], matches: dict[str, str], num_of_blocks: int) -> dict[str, str]:
    if len(blocks) == 0:
        return {}

    block = blocks[0]

    for i, char in enumerate(block.split('_')):
        if char in VARIABLES:
            s = s[i:]
            break
        if char == s[i]:
            block = '_'.join(block.split('_')[1:])

    block_type = get_block_type(block)

    if block_type == BlockType.xx_block:
        repetitions = list(set(find_xx_repetitions(s=s)))
        repetitions = [rep for rep in repetitions if (rep[0] == 0 or rep[0] == -1)]

        for repetition in repetitions:
            flag, new_s, variable, variable_match = match_xx_block_with_str(s, block, repetition=repetition)

            if not flag:
                continue

            if len(blocks) == 1 and new_s != '':
                continue

            matches[variable] = variable_match
            if new_s == '' and flag:
                return matches

            match_non_cross_pattern(s=new_s, blocks=blocks[1:], matches=matches, num_of_blocks=num_of_blocks)

            if len(matches) >= num_of_blocks:  # force выход из рекурсии
                return matches

    elif block_type == BlockType.xvx_block:
        v_substring = find_v_substring(block=block)
        repetitions = find_xvx_repetitions(s=s, v_substring=v_substring)

        for repetition in repetitions:
            flag, new_s, variable, variable_match = match_xvx_block_with_str(s=s, block=block, v_substring=v_substring,
                                                                             repetition=repetition)

            if not flag:
                continue

            if len(blocks) == 1 and new_s != '':
                continue

            matches[variable] = variable_match
            if new_s == '' and flag:
                return matches

            match_non_cross_pattern(s=new_s, blocks=blocks[1:], matches=matches, num_of_blocks=num_of_blocks)

            if len(matches) >= num_of_blocks:  # force выход из рекурсии
                return matches
    else:
        raise ValueError(f'Invalid block: {block}')

    return matches
