import random


from rep_var_patterns.match_rep_var_pattern import match_rep_var_pattern
from basic_generator import BasicGenerator
from models import CharType, VariableType, PatternCase


class RepVarPatternsGenerator(BasicGenerator):
    def generate(
            self, s_len: int, pattern_case: PatternCase, max_var_len: int = 10, k: int = 2
    ) -> tuple[str, str, dict[str, str]]:
        """Генерирует строку и шаблон для этой строки по заданному кейсу"""

        if pattern_case == PatternCase.random_case:
            s, pattern, matches = self.generate_random_case(s_len=s_len, max_var_len=max_var_len, k=k)

        elif pattern_case == PatternCase.hard_case:
            s, pattern, matches = self.generate_hard_case(s_len=s_len, max_var_len=max_var_len, k=k)

        else:
            raise ValueError(f'Invalid case name: {pattern_case}. Available cases: random_case, hard_case')

        return s, pattern, matches

    def generate_random_case(
            self, s_len: int, max_var_len: int, k: int, min_rep: int = 2, max_rep: int = 5
    ) -> tuple[str, str, dict[str, str]]:
        """Метод, который создаёт случайный шаблон с k повторяющимися переменной"""

        s = ''
        pattern = ''
        d = {}
        # словарь, в нём лежит кол-во раз, которое встретилась каждая из повторяющихся переменных
        rep_var_occurences = {}

        # set images for k repeatable variables
        for i in range(k):
            rep_var = self.variables[len(d)]
            rep_var_len = random.randint(1, max_var_len)
            rep_var_image = ''.join([random.choice(self.alphabet) for _ in range(rep_var_len)])
            d[rep_var] = rep_var_image
            rep_var_occurences[rep_var] = 0

        while len(s) < s_len:
            choice = random.choices([CharType.terminal, CharType.variable], weights=[0.2, 0.8])[0]

            if choice == CharType.terminal:
                char = random.choice(self.alphabet)
                s += char
                pattern += char if len(pattern) == 0 else f'_{char}'
            else:
                var_choice = random.choices([VariableType.usual, VariableType.repeatable], weights=[0.2, 0.8])[0]

                if var_choice == VariableType.usual:
                    usual_var = self.variables[len(d)]
                    usual_var_len = random.randint(1, max_var_len)
                    usual_var_image = ''.join(
                        [random.choice(self.alphabet) for _ in range(usual_var_len)])
                    d[usual_var] = usual_var_image  # добавил её мэтч в словарь

                    s += usual_var_image  # добавили изображение переменной в строку
                    pattern += usual_var if len(pattern) == 0 else f'_{usual_var}'

                else:
                    rep_var_choice = random.choices(list(rep_var_occurences.keys()))[0]  # выбираем встречающуюся переменную
                    s += d[rep_var_choice]
                    pattern += rep_var_choice if len(pattern) == 0 else f'_{rep_var_choice}'

                    rep_var_occurences[rep_var_choice] += 1

        for rep_var in rep_var_occurences:
            if rep_var_occurences[rep_var] < 2:
                split = 2 - rep_var_occurences[rep_var]
                for _ in range(split):
                    s += d[rep_var]
                    pattern += rep_var if len(pattern) == 0 else f'_{rep_var}'

        is_pattern_correct = self.check_pattern(s=s, pattern=pattern, matches=d)
        if not is_pattern_correct:
            raise ValueError(f'Invalid pattern!\nS: {s}, pattern: {pattern}, matches: {d}')

        return s, pattern, d
