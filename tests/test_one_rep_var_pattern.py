import pytest

from one_rep_var_patterns.match_one_rep_var_pattern import match_one_rep_var_pattern
from utils import check_pattern


@pytest.mark.parametrize('s, pattern, expect_success', [
    ('astkxciayvcgcaxnfkiwmownrcogjiwmownrcomownrcocjyagsfss', 'a_x2_i_a_y_v_x3_x1_x4_x1_x1_x5', True),
    ('pcpyzwltlpgddiswrctuoot', 'p_x2_x1_x1_x3_x4_x5', True),
    ('aabb', 'x1_x1_x2_x2', True),
    ('aababcaabacdaabade', 'a_x1_a_x2_a_x1_a_x3_a_x1_a_x4', True),
    ('aaaaaaaaaaaa', 'a_x1_a_x2_a_x1_a_x3_a_x1_a_x4', True),
    ('abbcaabcabbcbbcad', 'a_b_x1_a_a_x1_x2_b_c_x3_x1_a_x4', True)
])
def test_one_rep_pattern(s: str, pattern: str, expect_success: bool):
    matches = match_one_rep_var_pattern(s=s, pattern=pattern)
    result = check_pattern(s=s, pattern=pattern, matches=matches)
    assert result == expect_success
