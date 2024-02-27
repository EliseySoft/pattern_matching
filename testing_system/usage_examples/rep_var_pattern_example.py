from testing_system.rep_var_pattern_generator import RepVarPatternsGenerator
from rep_var_patterns.match_rep_var_pattern import match_rep_var_pattern
from testing_system.models import PatternCase
from testing_system.greedy_algorithm import greedy_matching_algorithm
from tqdm import tqdm


def usage_example():
    generator = RepVarPatternsGenerator()
    counter = 0

    ss = []
    patterns = []

    for _ in range(10):
        s, pattern, original_matches = generator.generate(s_len=50, pattern_case=PatternCase('random_case'), max_var_len=1, k=2)

        ss.append(s)
        patterns.append(pattern)

    for i in tqdm(range(len(patterns))):
        s = ss[i]
        pattern = patterns[i]

        matches = greedy_matching_algorithm(s=s, pattern=pattern)
        check_result = generator.check_pattern(s=s, pattern=pattern, matches=matches)

        if check_result:
            continue
        else:
            counter += 1
            print(f'Greedy error Error: s = {s}, pattern = {pattern}, matches = {matches}')

    for i in tqdm(range(len(patterns))):
        s = ss[i]
        pattern = patterns[i]

        matches = match_rep_var_pattern(s=s, pattern=pattern)
        check_result = generator.check_pattern(s=s, pattern=pattern, matches=matches)

        if check_result:
            continue
        else:
            counter += 1
            print(f'Error: s = {s}, pattern = {pattern}, matches = {matches}')

    if counter == 0:
        print('Ok!')


if __name__ == '__main__':
    usage_example()
