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
