from regular_pattern_generator import RegularPatternGenerator
from models import PatternCase
from regular_patterns.match_regular_pattern import match_regular_pattern


def usage_example():
    generator = RegularPatternGenerator()

    for i in range(20):
        s, pattern, original_matches = generator.generate(s_len=30 + i, pattern_case=PatternCase('hard_case'))
        print(f's: {s}')
        print(f'pattern: {pattern}')

        result, matches = match_regular_pattern(word=s, pattern=pattern)
        if result:
            check_result = generator.check_pattern(s=s, pattern=pattern, matches=matches)
            if check_result:
                print(f'Done!', end='\n\n')
            else:
                print(f'Error: s = {s}, pattern = {pattern}, original_matches = {original_matches}')


if __name__ == '__main__':
    usage_example()
