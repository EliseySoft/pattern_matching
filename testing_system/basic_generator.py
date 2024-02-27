from abc import ABC

from utils import ALPHABET, VARIABLES
from testing_system.models import PatternCase


class BasicGenerator(ABC):
    """Общий класс для всех генераторов строк и шаблонов."""

    alphabet: list[str] = sorted(list(ALPHABET))
    variables: list[str] = sorted(list(VARIABLES), key=lambda x: int(x[1:]))

    def generate(self, s_len: int, pattern_case: PatternCase, max_var_len: int = 10, **kwargs) -> tuple[str, str, dict[str, str]]:
        """Генерирует строку и шаблон для этой строки по заданному кейсу"""

        if pattern_case == PatternCase.random_case:
            s, pattern, matches = self.generate_random_case(s_len=s_len, max_var_len=max_var_len, **kwargs)

        elif pattern_case == PatternCase.hard_case:
            s, pattern, matches = self.generate_hard_case(s_len=s_len, max_var_len=max_var_len, **kwargs)

        else:
            raise ValueError(f'Invalid case name: {pattern_case}. Available cases: random_case, hard_case')

        return s, pattern, matches

    def generate_random_case(self, *args, **kwargs) -> tuple[str, str, dict[str, str]]:
        raise NotImplementedError('Random case generation not implemented!')

    def generate_hard_case(self, *args, **kwargs) -> tuple[str, str, dict[str, str]]:
        raise NotImplementedError('Random case generation not implemented!')

    @staticmethod
    def check_pattern(s: str, pattern: str, matches: dict[str, str]):
        """Проверяет, соответствует ли шаблон строке."""

        new_s = ''
        for char in pattern.split('_'):
            if char in VARIABLES:
                new_s += matches.get(char, '')
            else:
                new_s += char
        return new_s == s
