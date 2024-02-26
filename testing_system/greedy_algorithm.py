# def greedy_algorithm(s: str, pattern: str) -> dict[str, str]:
#     pass

# У меня есть строка, состоящая из английских букв в нижнем регистре. Для этой строки есть шаблон. Шаблон это такая же строка, которая состоит из букв и переменных. Твоя задача найти значения этих переменных, чтобы шаблон стал равен строке. Переменные могут быть равны одной или нескольким буквам.
# Реализуй жадный алгоритм на питоне, который будет перебирать все варианты возможных значений  и возвращать значения для переменных в виде словаря


def word_pattern(pattern: str, word: str) -> bool:
    """Given a pattern string, check if 'word' can match pattern.
    'Match' here means a bijection between each character in pattern
    with a nonempty substring in word.
    """

    pattern_len = len(pattern)
    word_len = len(word)

    def dfs(biject_pat_to_word: dict[str, str],
            already_used_strs: set[str],
            pattern_index: int,
            word_index: int) -> bool:
        """Greedily try to match each pattern character to the shortest
        possible substring of word, consistent with current bijection.
        Return whether this was possible."""

        if pattern_index == pattern_len:  # Reached pattern end
            return word_index == word_len
        next_letter = pattern[pattern_index]

        # If we've already seen this pattern char, it must match again
        if next_letter in biject_pat_to_word:
            pat_match = biject_pat_to_word[next_letter]
            if word[word_index:word_index + len(pat_match)] != pat_match:
                return False

            word_index += len(pat_match)
            pattern_index += 1

            return dfs(biject_pat_to_word, already_used_strs,
                       pattern_index, word_index)

        curr_str_match = ''
        for amount_to_take in range(1, word_len - word_index + 1):
            curr_str_match += word[word_index + amount_to_take - 1]
            if curr_str_match in already_used_strs:
                continue

            biject_pat_to_word[next_letter] = curr_str_match
            already_used_strs.add(curr_str_match)

            # Try to use this pattern
            if dfs(biject_pat_to_word, already_used_strs,
                   pattern_index=pattern_index + 1,
                   word_index=word_index + amount_to_take):
                return True

            already_used_strs.discard(curr_str_match)

        # If we've set which string we match, unset it for future calls
        if next_letter in biject_pat_to_word:
            del biject_pat_to_word[next_letter]

        return False

    return dfs(biject_pat_to_word={},
               already_used_strs=set(),
               pattern_index=0, word_index=0)


    s = 'hibiehi'
    pattern = 'ABA'
    result = word_pattern(pattern=pattern, word=s)
    print(result)
