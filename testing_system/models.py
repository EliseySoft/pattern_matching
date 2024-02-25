from enum import Enum


class CharType(Enum):
    """Класс, описывающий тип символа: терминал или переменная."""

    terminal: str = 'terminal'
    variable: str = 'variable'


class PatternCase(Enum):
    """
    Класс, описывающий случай кейса: случайный и сложный.
    """

    random_case: str = 'random_case'
    hard_case: str = 'hard_case'


class NonCrossBlockType(Enum):
    """Класс, описывающий два случая блоков в непересекающихся шаблонах."""

    xvx_case: str = 'xvx_case'
    xx_case: str = 'xx_case'


class VariableType(Enum):
    """Класс, описывающий тип переменной: повторяющася или обычныя"""
    repeatable: str = 'repeatable'
    usual: str = 'usual'
