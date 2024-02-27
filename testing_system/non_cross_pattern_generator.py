import random

from testing_system.basic_generator import BasicGenerator
from testing_system.models import CharType, PatternCase, NonCrossBlockType


class NonCrossPatternGenerator(BasicGenerator):
    """Генератор для непересекающихся шаблонов и строк к ним."""

    def generate_xx_block(
            self, max_var_len: int, max_block_len: int, d: dict[str, str]
    ) -> tuple[str, str, dict[str, str]]:
        """Метод, который создаёт блок типа xx"""

        block_s: str = ''
        block_pattern: str = ''

        block_len = random.randint(2, max_block_len)

        variable = self.variables[len(d)]
        # для случая хх длина переменной <= (block_len // 2)
        var_len = random.randint(0, min(max_var_len, block_len // 2))
        var_match = ''.join([random.choice(self.alphabet) for _ in range(var_len)])
        d[variable] = var_match

        block_s += (var_match + var_match)
        block_pattern += f'{variable}_{variable}'

        while len(block_s) < block_len:
            choice = random.choices([CharType.terminal, CharType.variable], weights=[0.6, 0.4])[0]

            if choice == CharType.terminal:
                char = random.choice(self.alphabet)
                block_s += char
                block_pattern += f'_{char}'
            else:
                block_s += var_match
                block_pattern += f'_{variable}'

        return block_s, block_pattern, d

    def generate_xvx_block(
            self, max_var_len: int, max_block_len: int, d: dict[str, str]
    ) -> tuple[str, str, dict[str, str]]:
        """Метод, который создаёт блок типа xvx"""
        block_s: str = ''
        block_pattern: str = ''

        block_len = random.randint(3, max_block_len)
        v_substring_len = random.randint(1, block_len - 2)
        v_substring = ''.join([random.choice(self.alphabet) for _ in range(v_substring_len)])

        variable = self.variables[len(d)]
        # для случая хvх длина переменной <= ((block_len - v_substring_len) // 2)
        var_len = random.randint(0, min(max_var_len, (block_len - v_substring_len) // 2))
        var_match = ''.join([random.choice(self.alphabet) for _ in range(var_len)])
        d[variable] = var_match

        block_s += (var_match + v_substring + var_match)
        block_pattern += f'{variable}_{"_".join(v_substring)}_{variable}'

        while len(block_s) < block_len:
            choice = random.choices([CharType.terminal, CharType.variable], weights=[0.8, 0.2])[0]

            if choice == CharType.terminal:
                char = random.choice(self.alphabet)
                block_s += char
                block_pattern += f'_{char}'
            else:
                block_s += var_match
                block_pattern += f'_{variable}'

        return block_s, block_pattern, d

    def generate_random_case(self, s_len: int, max_var_len: int, max_block_len: int) -> tuple[str, str, dict[str, str]]:
        """Метод, который создаёт случайный шаблон с непересекающимися переменными"""

        s = ''
        pattern = ''
        d = {}

        while len(s) < s_len:
            block_type = random.choices([NonCrossBlockType.xx_case, NonCrossBlockType.xvx_case], weights=[0.5, 0.5])[0]

            if block_type == NonCrossBlockType.xx_case:
                block_s, block_pattern, d = self.generate_xx_block(max_var_len, max_block_len, d)
                s += block_s
                if len(pattern) == 0:
                    pattern += block_pattern
                else:
                    pattern += f'_{block_pattern}'

            else:
                block_s, block_pattern, d = self.generate_xvx_block(max_var_len, max_block_len, d)
                s += block_s
                if len(pattern) == 0:
                    pattern += block_pattern
                else:
                    pattern += f'_{block_pattern}'

        is_pattern_correct = self.check_pattern(s=s, pattern=pattern, matches=d)
        if not is_pattern_correct:
            raise ValueError(f'Invalid pattern!\nS: {s}, pattern: {pattern}, matches: {d}')

        return s, pattern, d

    def generate_hard_case(self, s_len: int, max_var_len: int, max_block_len: int) -> tuple[str, str, dict[str, str]]:
        """
        Метод, который создаёт сложный случай шаблона и строки для него.
        А какой сложный случай то тут можно придумать?...
        """
        pass

    def generate(
            self, s_len: int, pattern_case: PatternCase, max_var_len: int = 10, max_block_len: int = 10
    ) -> tuple[str, str, dict[str, str]]:
        """Генерирует строку и шаблон для этой строки по заданному кейсу"""

        if pattern_case == PatternCase.random_case:
            s, pattern, matches = self.generate_random_case(
                s_len=s_len, max_var_len=max_var_len, max_block_len=max_block_len
            )

        elif pattern_case == PatternCase.hard_case:
            s, pattern, matches = self.generate_hard_case(
                s_len=s_len, max_var_len=max_var_len, max_block_len=max_block_len
            )

        else:
            raise ValueError(f'Invalid case name: {pattern_case}. Available cases: random_case, hard_case')

        return s, pattern, matches
