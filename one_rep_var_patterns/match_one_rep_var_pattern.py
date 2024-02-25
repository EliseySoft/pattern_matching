from one_rep_var_patterns.suffix_array import build_suffix_array, get_longest_common_prefix, split_suffix_array
from regular_patterns.match_regular_pattern import match_regular_pattern
from utils import VARIABLES, check_pattern


def parse_one_rep_var_pattern(one_rep_var_pattern: str) -> list[str]:
    blocks = []
    chars = one_rep_var_pattern.split('_')
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


def count_rep_var(parsed_pattern: list[str]) -> tuple[str, int]:
    """Возвращает повторяющуюся переменную и количество раз, которые она встречается"""
    d = {}
    for char in parsed_pattern:
        if char in VARIABLES:
            d[char] = d.get(char, 0) + 1

    for var in d:
        if d[var] > 1:
            return var, d[var]


def match_one_rep_var_pattern(s: str, pattern: str) -> dict[str, str]:
    # matches = []
    suffix_array = build_suffix_array(s=s)
    prefixes_lens = [get_longest_common_prefix(suffix_array, s, i, i + 1) for i in range(len(suffix_array) - 1)]

    parsed_pattern = parse_one_rep_var_pattern(one_rep_var_pattern=pattern)
    rep_var, counter = count_rep_var(parsed_pattern=parsed_pattern)

    for l in range(1, len(s)):
        clusters = split_suffix_array(suffix_array=suffix_array, common_prefix_lens=prefixes_lens, l=l)
        clusters = [cluster for cluster in clusters if len(cluster) >= counter]

        for cluster in clusters:
            rep_var_image = s[cluster[0]:cluster[0] + l]
            d = {rep_var: rep_var_image}

            regular_pattern = '_'.join([rep_var_image if char == rep_var else char for char in pattern.split('_')])
            try:
                result, match = match_regular_pattern(word=s, regular_pattern=regular_pattern)
            except AssertionError:  # может быть не состыковка в сопоставлении, поэтому используем try/except
                continue

            if result:
                d.update(match)
                # matches.append(d)
                return d

    # return matches
    return {}


if __name__ == '__main__':
    word = 'astkxciayvcgcaxnfkiwmownrcogjiwmownrcomownrcocjyagsfss'
    pattern = 'a_x2_i_a_y_v_x3_x1_x4_x1_x1_x5'
    # original_matches: {'x1': 'mownrco', 'x2': 'stkxc', 'x3': 'cgcaxnfkiw', 'x4': 'gjiw', 'x5': 'cjyagsfss'}
    matches = match_one_rep_var_pattern(s=word, pattern=pattern)
    pattern_is_correct = check_pattern(s=word, pattern=pattern, matches=matches)
    if pattern_is_correct:
        print('Ok!')
    else:
        print('Incorrect match!')

#     word = 'pcpyzwltlpgddiswrctuoot'
#     pattern = 'p_x2_x1_x1_x3_x4_x5'
#     # original_matches = {'x1': 'ar', 'x2': 'ehwrjkyaac', 'x3': 'fxb', 'x4': 'h', 'x5': 'yilxdlnkc'}
#     matches = match_one_rep_var_pattern(s=word, pattern=pattern)
#     pattern_is_correct = check_pattern(s=word, pattern=pattern, matches=matches)
#     if pattern_is_correct:
#         print('Ok!')
#     else:
#         print('Incorrect match!')

    # word = 'aabb'
    # pattern = 'x1_x1_b_b'
    # matches = match_one_rep_var_pattern(s=word, pattern=pattern)
    # print(matches)

    # word = 'aababcaabacdaabade'
    # pattern = 'a_x1_a_x2_a_x1_a_x3_a_x1_a_x4'
    # matches = match_one_rep_var_pattern(s=word, pattern=pattern)
    # print(matches)

    # word = 'aaaaaaaaaaaa'
    # pattern = 'a_x1_a_x2_a_x1_a_x3_a_x1_a_x4'
    # matches = match_one_rep_var_pattern(s=word, pattern=pattern)
    # print(matches)

    # word = 'abbcaabcabbcbbcad'
    # pattern = 'a_b_x1_a_a_x1_x2_b_c_x3_x1_a_x4'
    # matches = match_one_rep_var_pattern(s=word, pattern=pattern)
    # print(matches)
