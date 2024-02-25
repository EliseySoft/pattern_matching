def build_suffix_array(s):
    n = len(s)
    suffixes = [(s[i:], i) for i in range(n)]
    suffixes.sort()

    suffix_array = [suffix[1] for suffix in suffixes]

    return suffix_array


def get_longest_common_prefix(suffix_array, s, i, j):
    common_prefix = 0

    while True:
        if s[suffix_array[i] + common_prefix] == s[suffix_array[j] + common_prefix]:
            common_prefix += 1
        else:
            break

        if suffix_array[i] + common_prefix == len(s) or suffix_array[j] + common_prefix == len(s):
            break

    return common_prefix


def split_suffix_array(suffix_array: list[int], common_prefix_lens: list[int], l: int) -> list[list[int]]:
    """Функция, которая делит суффиксный массив на кластеры"""

    clusters = []
    curr_cluster = []
    for i in range(len(common_prefix_lens)):
        if common_prefix_lens[i] == 0:
            if curr_cluster:
                clusters.append(curr_cluster)
                curr_cluster = []
            continue
        elif common_prefix_lens[i] >= l:
            if not curr_cluster:
                curr_cluster.append(suffix_array[i])
                curr_cluster.append(suffix_array[i + 1])
            else:
                curr_cluster.append(suffix_array[i + 1])
        else:
            if curr_cluster:
                clusters.append(curr_cluster)
                curr_cluster = []
    if curr_cluster:
        clusters.append(curr_cluster)
    return clusters
