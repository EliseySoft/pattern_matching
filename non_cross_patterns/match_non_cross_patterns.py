from enum import Enum

from non_cross_xx.match_xx_patterns import match_xx_patterns, find_xx_repetitions, match_xx_block_with_str
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
        repetitions = [rep for rep in repetitions if rep[0] == 0]

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

            matches[variable] = variable_match
            if new_s == '' and flag:
                return matches

            match_non_cross_pattern(s=new_s, blocks=blocks[1:], matches=matches, num_of_blocks=num_of_blocks)

            if len(matches) >= num_of_blocks:  # force выход из рекурсии
                return matches
    else:
        raise ValueError(f'Invalid block: {block}')

    return matches


def test():
    s = 'fffpepepepepepeosdosdosdosd'
    pattern = 'x1_x1_x1_x2_x2_x2_x2_x2_x2_x3_x3_x3_x3'
    blocks = parse_pattern(pattern)
    matches = match_non_cross_pattern(s=s, blocks=blocks, matches={}, num_of_blocks=len(blocks))
    print(matches, end='\n\n')
    result = check_pattern(s=s, pattern=pattern, matches=matches)
    assert result == True

    s = 'ttbtnixrrtpnmssjssjmnfccmzmuoll'
    pattern = 'x1_x1_b_x1_x2_i_x_r_r_t_p_x2_m_x3_x3_x4_n_f_c_c_m_z_x4_u_o_l_l'
    blocks = parse_pattern(pattern)
    matches = match_non_cross_pattern(s=s, blocks=blocks, matches={}, num_of_blocks=len(blocks))
    print(matches, end='\n\n')
    result = check_pattern(s=s, pattern=pattern, matches=matches)
    assert result == True

    s = 'ydnbpbtydgolwlwlwlwdsqdlgs'
    pattern = 'x1_n_b_p_b_t_x1_g_o_x2_x2_x2_x2_x3_s_q_x3_l_g_s'
    blocks = parse_pattern(pattern)
    matches = match_non_cross_pattern(s=s, blocks=blocks, matches={}, num_of_blocks=len(blocks))
    print(matches, end='\n\n')
    result = check_pattern(s=s, pattern=pattern, matches=matches)
    assert result == True

    s = 'kfofdcaokfkfyywyywff'
    pattern = 'x1_o_f_d_c_a_o_x1_x1_x2_x2_x3_x3'
    blocks = parse_pattern(pattern)
    matches = match_non_cross_pattern(s=s, blocks=blocks, matches={}, num_of_blocks=len(blocks))
    print(matches, end='\n\n')
    result = check_pattern(s=s, pattern=pattern, matches=matches)
    assert result == True

    s = 'ghghjshaghalttzttzbagjbbagjbagjbagj'
    pattern = 'x1_x1_j_s_h_a_x1_a_l_x2_x2_x3_b_x3_x3_x3'
    blocks = parse_pattern(pattern)
    matches = match_non_cross_pattern(s=s, blocks=blocks, matches={}, num_of_blocks=len(blocks))
    print(matches, end='\n\n')
    result = check_pattern(s=s, pattern=pattern, matches=matches)
    assert result == True

    s = 'ststskckckckcgpfjgpfjdgpfjv'
    pattern = 'x1_t_s_t_x1_x2_x2_x2_x2_x3_x3_d_x3_v'
    blocks = parse_pattern(pattern)
    matches = match_non_cross_pattern(s=s, blocks=blocks, matches={}, num_of_blocks=len(blocks))
    print(matches, end='\n\n')
    result = check_pattern(s=s, pattern=pattern, matches=matches)
    assert result == True

    s = 'xuujoyrxuueejvbeejvbeejvb'
    pattern = 'x1_j_o_y_r_x1_x2_x2_x2'
    blocks = parse_pattern(pattern)
    matches = match_non_cross_pattern(s=s, blocks=blocks, matches={}, num_of_blocks=len(blocks))
    print(matches, end='\n\n')
    result = check_pattern(s=s, pattern=pattern, matches=matches)
    assert result == True

    s = 'ababababbcabcbcbce'
    pattern = 'x1_x1_a_b_x1_x2_a_b_c_x2_x2_e'
    blocks = parse_pattern(pattern)
    matches = match_non_cross_pattern(s=s, blocks=blocks, matches={}, num_of_blocks=len(blocks))
    print(matches, end='\n\n')
    result = check_pattern(s=s, pattern=pattern, matches=matches)
    assert result == True

    s = 'aabcaababde'
    pattern = 'x1_a_b_c_x1_x2_x2_d_e'
    blocks = parse_pattern(pattern)
    matches = match_non_cross_pattern(s=s, blocks=blocks, matches={}, num_of_blocks=len(blocks))
    print(matches, end='\n\n')
    result = check_pattern(s=s, pattern=pattern, matches=matches)
    assert result == True

    s = 'abcabcabcabcabcdeababaabab'
    pattern = 'a_b_c_x1_a_b_c_x1_x1_d_e_x2_x2_a_x2_x2'
    blocks = parse_pattern(pattern)
    matches = match_non_cross_pattern(s=s, blocks=blocks, matches={}, num_of_blocks=len(blocks))
    print(matches, end='\n\n')
    result = check_pattern(s=s, pattern=pattern, matches=matches)
    assert result == True

    s = 'abababbcbcbce'
    pattern = 'x1_x1_x1_x2_x2_x2_e'
    blocks = parse_pattern(pattern)
    matches = match_non_cross_pattern(s=s, blocks=blocks, matches={}, num_of_blocks=len(blocks))
    print(matches, end='\n\n')
    result = check_pattern(s=s, pattern=pattern, matches=matches)
    assert result == True

    s = 'aaaaaaaaabaabbe'
    pattern = 'x1_a_x1_a_x1_a_x2_a_a_x2_x2_e'
    blocks = parse_pattern(pattern)
    matches = match_non_cross_pattern(s=s, blocks=blocks, matches={}, num_of_blocks=len(blocks))
    print(matches, end='\n\n')
    result = check_pattern(s=s, pattern=pattern, matches=matches)
    assert result == True

    s = 'aaaaaaaaabbaabbbbe'
    pattern = 'x1_a_x1_a_x1_a_x2_a_a_x2_x2_e'
    blocks = parse_pattern(pattern)
    matches = match_non_cross_pattern(s=s, blocks=blocks, matches={}, num_of_blocks=len(blocks))
    print(matches, end='\n\n')
    result = check_pattern(s=s, pattern=pattern, matches=matches)
    assert result == True

    s = 'aaaaaaaaaabaabbe'
    pattern = 'x1_x1_x1_a_x1_a_a_a_a_a_x2_a_a_x2_x2_e'
    blocks = parse_pattern(pattern)
    matches = match_non_cross_pattern(s=s, blocks=blocks, matches={}, num_of_blocks=len(blocks))
    print(matches, end='\n\n')
    result = check_pattern(s=s, pattern=pattern, matches=matches)
    assert result == True

    s = 'aaaaaaaaaaaae'
    pattern = 'x1_x1_x1_x2_x2_x2_e'
    blocks = parse_pattern(pattern)
    matches = match_non_cross_pattern(s=s, blocks=blocks, matches={}, num_of_blocks=len(blocks))
    print(matches, end='\n\n')
    result = check_pattern(s=s, pattern=pattern, matches=matches)
    assert result == True


if __name__ == '__main__':
    test()
