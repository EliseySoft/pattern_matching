import string

ALPHABET = set(list(string.ascii_lowercase))
VARIABLES = set([f'x{i}' for i in range(1, 1001)])


def parse_pattern(pattern: str) -> list[str]:
    one_variable_blocks = []
    prev_variable = None
    curr_block = ''

    for char in pattern.split('_'):
        if char in VARIABLES:  # встретили переменную
            if prev_variable == char or prev_variable is None:  # встретили переменную из текущего блока
                curr_block += f'_{char}' if len(curr_block) > 0 else char
                prev_variable = char
            else:  # встретили переменную из нового блока
                prev_variable = char
                if curr_block != '':
                    one_variable_blocks.append(curr_block)
                curr_block = char
        elif char in ALPHABET:  # встретили терминал
            curr_block += f'_{char}' if len(curr_block) > 0 else char
        else:
            raise ValueError(f'Invalid character: {char}')

    if len(curr_block) > 0:
        one_variable_blocks.append(curr_block)

    return one_variable_blocks


def check_pattern(s: str, pattern: str, matches: dict[str, str]) -> bool:
    new_s = ''
    for char in pattern.split('_'):
        if char in VARIABLES:
            new_s += matches.get(char, '')
        else:
            new_s += char
    return new_s == s


def test_parse_pattern():
    test1 = 'a_a_a_x1_x1_x2_x2_b'
    expected_output1 = ['a_a_a_x1_x1', 'x2_x2_b']
    output1 = parse_pattern(test1)
    assert output1 == expected_output1

    test2 = 'x1_x1_x1_x1_x2_x2'
    expected_output2 = ['x1_x1_x1_x1', 'x2_x2']
    output2 = parse_pattern(test2)
    assert output2 == expected_output2

    test3 = 'x1_x2'
    expected_output3 = ['x1', 'x2']
    output3 = parse_pattern(test3)
    assert output3 == expected_output3

    test4 = 'x1_x1_x1_x1_x2_x2_x3_x3_x4'
    expected_output4 = ['x1_x1_x1_x1', 'x2_x2', 'x3_x3', 'x4']
    output4 = parse_pattern(test4)
    assert output4 == expected_output4

    test5 = 'x1_x1_x1_x1_x1'
    expected_output5 = ['x1_x1_x1_x1_x1']
    output5 = parse_pattern(test5)
    assert output5 == expected_output5

    test6 = 'a_x1_a_x1_x2_a_x2_a_a_a_x2_a_x3_x3_x3_b'
    expected_output6 = ['a_x1_a_x1', 'x2_a_x2_a_a_a_x2_a', 'x3_x3_x3_b']
    output6 = parse_pattern(test6)
    assert output6 == expected_output6

    test7 = 'a_x1_a_x1_a_a_a_x1_a_x1_a_x1'
    expected_output7 = ['a_x1_a_x1_a_a_a_x1_a_x1_a_x1']
    output7 = parse_pattern(test7)
    assert output7 == expected_output7

    print('All tests passed! ✅✅✅')


if __name__ == '__main__':
    test_parse_pattern()
