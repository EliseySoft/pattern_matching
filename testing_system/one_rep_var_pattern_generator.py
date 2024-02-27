import random

from testing_system.basic_generator import BasicGenerator
from testing_system.models import CharType, VariableType, PatternCase


class OneRepVarPatternGenerator(BasicGenerator):
    """Генератор для шаблонов с одной повторяющейся переменной и строк к ним"""

    def generate(
            self, s_len: int, pattern_case: PatternCase, max_var_len: int = 10, min_rep: int = 2, max_rep: int = 5
    ) -> tuple[str, str, dict[str, str]]:
        """Генерирует строку и шаблон для этой строки по заданному кейсу"""

        if pattern_case == PatternCase.random_case:
            s, pattern, matches = self.generate_random_case(
                s_len=s_len, max_var_len=max_var_len, min_rep=min_rep, max_rep=max_rep
            )

        elif pattern_case == PatternCase.hard_case:
            s, pattern, matches = self.generate_hard_case(s_len=s_len, max_var_len=max_var_len)

        else:
            raise ValueError(f'Invalid case name: {pattern_case}. Available cases: random_case, hard_case')

        return s, pattern, matches

    def generate_random_case(
            self, s_len: int, max_var_len: int, min_rep: int = 2, max_rep: int = 5
    ) -> tuple[str, str, dict[str, str]]:
        """Метод, который создаёт случайный шаблон с одной повторяющейся переменной"""

        s = ''
        pattern = ''
        d = {}

        number_of_repetitions = random.randint(min_rep, max_rep)

        rep_var = 'x1'
        rep_var_len = random.randint(1, max_var_len)
        rep_var_image = ''.join([random.choice(self.alphabet) for _ in range(rep_var_len)])
        d[rep_var] = rep_var_image
        num_of_rep_var_occurences = 0

        while len(s) < s_len:
            choice = random.choices([CharType.terminal, CharType.variable])[0]

            if choice == CharType.terminal:
                char = random.choice(self.alphabet)
                s += char
                pattern += char if len(pattern) == 0 else f'_{char}'
            else:
                var_choice = random.choices([VariableType.usual, VariableType.repeatable])[0]

                if var_choice == VariableType.usual:
                    usual_var = self.variables[len(d)]  # взяли новую переменную
                    usual_var_len = random.randint(1, max_var_len)  # определили её длину
                    usual_var_image = ''.join([random.choice(self.alphabet) for _ in range(usual_var_len)])  # определили её изображение
                    d[usual_var] = usual_var_image  # добавил её мэтч в словарь

                    s += usual_var_image  # добавили изображение переменной в строку
                    pattern += usual_var if len(pattern) == 0 else f'_{usual_var}'  # добавили переменную в шаблон

                else:
                    num_of_rep_var_occurences += 1
                    s += rep_var_image
                    pattern += rep_var if len(pattern) == 0 else f'_{rep_var}'

        if num_of_rep_var_occurences < number_of_repetitions:
            split = number_of_repetitions - num_of_rep_var_occurences

            for _ in range(split):
                s += rep_var_image
                pattern += rep_var if len(pattern) == 0 else f'_{rep_var}'
                num_of_rep_var_occurences += 1

        if len(d) == 1:  # всего одна переменная, и та повторяющаяся, надо добавить одну дополнительную переменную
            usual_var = self.variables[len(d)]  # взяли новую переменную
            usual_var_len = random.randint(1, max_var_len)  # определили её длину
            usual_var_image = ''.join(
                [random.choice(self.alphabet) for _ in range(usual_var_len)])  # определили её изображение
            d[usual_var] = usual_var_image  # добавил её мэтч в словарь

            s += usual_var_image  # добавили изображение переменной в строку
            pattern += usual_var if len(pattern) == 0 else f'_{usual_var}'  # добавили переменную в шаблон

        is_pattern_correct = self.check_pattern(s=s, pattern=pattern, matches=d)
        if not is_pattern_correct:
            raise ValueError(f'Invalid pattern!\nS: {s}, pattern: {pattern}, matches: {d}')

        return s, pattern, d
