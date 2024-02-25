from utils import ALPHABET


def match_one_var_pattern(
        word: str, pattern: str, var_char: str = 'x1'
) -> tuple[bool, dict[str, str]] | tuple[bool, None]:
    new_var_char = 'X'
    pattern = pattern.replace(var_char, new_var_char)
    pattern = ''.join(pattern.split('_'))

    num_terminals_in_word = len(word)
    num_terminals_in_pattern = sum(1 for char in pattern if char != new_var_char)
    num_variables_in_pattern = len(pattern) - num_terminals_in_pattern
    if num_variables_in_pattern == 0:
        if pattern == word:
            return True, {}
        else:
            return False, None
    var_len = (num_terminals_in_word - num_terminals_in_pattern) // num_variables_in_pattern
    var_index = -1

    for i in range(len(word)):
        if word[i] == pattern[i]:
            continue
        elif pattern[i] in ALPHABET and pattern[i] != new_var_char:
            return False, None
        else:
            var_index = i
            break

    var_match = word[var_index:var_index + var_len]
    pattern_to_string = ''

    for i in range(len(pattern)):
        pattern_to_string += pattern[i] if pattern[i] != new_var_char else var_match

    if pattern_to_string != word:
        return False, None

    if var_match == '':
        return False, None

    return True, {var_char: var_match}


# if __name__ == '__main__':
#     word = 'aabaabaab'
#     pattern = 'a_x1_a_x1_a_x1'
#     print(match_one_var_pattern(word=word, pattern=pattern, var_char='x1'))
