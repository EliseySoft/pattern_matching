import random

from regular_patterns.match_regular_pattern import match_regular_pattern
from basic_generator import BasicGenerator
from models import CharType, PatternCase


class RegularPatternGenerator(BasicGenerator):
    """Генератор для регулярных шаблонов и строк к ним."""

    def generate_random_case(self, s_len: int, max_var_len: int) -> tuple[str, str, dict[str, str]]:
        """Метод, которая создаёт случайную строку и однопеременный шаблон для неё."""

        s = ''
        pattern = ''
        d = {}

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
                variable = self.variables[len(d)]
                var_len = random.randint(0, max_var_len)
                var_match = ''.join([random.choice(self.alphabet) for _ in range(var_len)])
                d[variable] = var_match

                s += var_match
                if len(pattern) == 0:
                    pattern += variable
                else:
                    pattern += f'_{variable}'

        if len(d) == 0:  # на случай, если в шаблоне вдруг нет переменных
            variable = self.variables[len(d)]
            var_len = random.randint(0, max_var_len)
            var_match = ''.join([random.choice(self.alphabet) for _ in range(var_len)])
            d[variable] = var_match

            s += var_match
            if len(pattern) == 0:
                pattern += variable
            else:
                pattern += f'_{variable}'

        pattern_is_correct = self.check_pattern(s=s, pattern=pattern, matches=d)
        if not pattern_is_correct:
            raise ValueError(f'Invalid pattern!\nS: {s}, pattern: {pattern}, matches: {d}')

        return s, pattern, d

    def generate_hard_case(self, s_len: int, max_var_len: int) -> tuple[str, str, dict[str, str]]:
        """
        Метод, который создаёт сложный случай строки и регулярного шаблона для неё.
        Сложность случая заключается в том, что в нём находится как можно больше переменных.
        Таким образом, реализованный алгоритм будет также работать за время O(|w| + |a|).
        При этом жадному алгоритму придётся подбирать для каждой переменной своё изображение,
        что будет неэффективно по времени, так как алгоритм жадный.
        """

        s = ''
        pattern = ''
        d = {}

        while len(s) < s_len:
            choice = random.choices([CharType.terminal, CharType.variable], weights=[0.5, 0.5])[0]

            if choice == CharType.terminal:
                char = random.choice(self.alphabet)
                s += char
                if len(pattern) == 0:
                    pattern += char
                else:
                    pattern += f'_{char}'
            else:
                variable = self.variables[len(d)]
                var_len = random.randint(0, max_var_len)
                var_match = ''.join([random.choice(self.alphabet) for _ in range(var_len)])
                d[variable] = var_match

                s += var_match
                if len(pattern) == 0:
                    pattern += variable
                else:
                    pattern += f'_{variable}'

        if len(d) == 0:  # на случай, если в шаблоне вдруг нет переменных
            variable = self.variables[len(d)]
            var_len = random.randint(0, max_var_len)
            var_match = ''.join([random.choice(self.alphabet) for _ in range(var_len)])
            d[variable] = var_match

            s += var_match
            if len(pattern) == 0:
                pattern += variable
            else:
                pattern += f'_{variable}'

        pattern_is_correct = self.check_pattern(s=s, pattern=pattern, matches=d)
        if not pattern_is_correct:
            raise ValueError(f'Invalid pattern!\nS: {s}, pattern: {pattern}, matches: {d}')

        return s, pattern, d
