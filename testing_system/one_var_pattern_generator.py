import random

from one_var_patterns.match_one_var_pattern import match_one_var_pattern
from basic_generator import BasicGenerator
from models import PatternCase
from models import CharType


class OneVarPatternGenerator(BasicGenerator):
    """Генератор для шаблонов с одной переменной и строк к ним."""

    def generate_random_case(self, s_len: int, max_var_len: int) -> tuple[str, str, dict[str, str]]:
        """Метод, который создаёт случайную строку и регулярный шаблон для неё."""

        s = ''
        pattern = ''
        d = {}

        variable = 'x1'
        var_len = random.randint(1, max_var_len)
        var_match = ''.join([random.choice(self.alphabet) for _ in range(var_len)])
        d[variable] = var_match

        while len(s) < s_len:
            choice = random.choices([CharType.terminal, CharType.variable], weights=[0.67, 0.33])[0]

            if choice == CharType.terminal:
                char = random.choice(self.alphabet)
                s += char
                if len(pattern) == 0:
                    pattern += char
                else:
                    pattern += f'_{char}'
            else:
                s += var_match
                if len(pattern) == 0:
                    pattern += variable
                else:
                    pattern += f'_{variable}'

        if variable not in pattern:  # вдруг переменная не добавилась
            s += var_match
            pattern += f'_{variable}'

        pattern_is_correct = self.check_pattern(s=s, pattern=pattern, matches=d)
        if not pattern_is_correct:
            raise ValueError(f'Invalid pattern!\nS: {s}, pattern: {pattern}, matches: {d}')

        return s, pattern, d

    def generate_hard_case(self, s_len: int, max_var_len: int) -> tuple[str, str, dict[str, str]]:
        """
            Метод, который создаёт случайную строку и сложный случай однопеременного шаблона для неё.
            Это случай, в котором в самом начале точно стоит переменная.
            В таком случае алгоритму придётся подбирать,
            а затем проходиться по оставшейся строке за O(N) от каждого подбора.
        """

        s = ''
        pattern = ''
        d = {}

        variable = 'x1'
        var_len = random.randint(1, max_var_len)
        var_match = ''.join([random.choice(self.alphabet) for _ in range(var_len)])
        d[variable] = var_match

        s += var_match
        pattern += variable

        while len(s) < s_len:
            choice = random.choices([CharType.terminal, CharType.variable], weights=[0.33, 0.67])[0]

            if choice == CharType.terminal:
                char = random.choice(self.alphabet)
                s += char
                if len(pattern) == 0:
                    pattern += char
                else:
                    pattern += f'_{char}'
            else:
                s += var_match
                if len(pattern) == 0:
                    pattern += variable
                else:
                    pattern += f'_{variable}'

        if variable not in pattern:  # вдруг переменная не добавилась
            s += var_match
            pattern += f'_{variable}'

        pattern_is_correct = self.check_pattern(s=s, pattern=pattern, matches=d)

        if not pattern_is_correct:
            raise ValueError(f'Invalid pattern!\nS: {s}, pattern: {pattern}, matches: {d}')

        return s, pattern, d
