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
    """Функция, которая мэтчит строку с одной повторяющейся переменной с шаблоном."""

    # matches = []
    suffix_array = build_suffix_array(s=s)
    prefixes_lens = [get_longest_common_prefix(suffix_array, s, i, i + 1) for i in range(len(suffix_array) - 1)]

    parsed_pattern = parse_one_rep_var_pattern(one_rep_var_pattern=pattern)
    rep_var, counter = count_rep_var(parsed_pattern=parsed_pattern)

    # повторяющаяся переменная равна пустой строке
    rep_var_image = ''
    d = {rep_var: rep_var_image}
    pattern_chars = pattern.split('_')

    regular_pattern = '_'.join([char for char in pattern_chars if char != rep_var])

    matches = match_regular_pattern(s=s, pattern=regular_pattern)

    if len(matches) != 0:
        d.update(matches)
        return d

    for l in range(1, len(s)):
        clusters = split_suffix_array(suffix_array=suffix_array, common_prefix_lens=prefixes_lens, l=l)
        clusters = [cluster for cluster in clusters if len(cluster) >= counter]

        for cluster in clusters:
            rep_var_image = s[cluster[0]:cluster[0] + l]
            d = {rep_var: rep_var_image}

            regular_pattern = '_'.join([rep_var_image if char == rep_var else char for char in pattern.split('_')])

            matches = match_regular_pattern(s=s, pattern=regular_pattern)

            if len(matches) != 0:
                d.update(matches)
                return d

    # return matches
    return {}
