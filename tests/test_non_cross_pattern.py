import pytest

from non_cross_patterns.match_non_cross_patterns import match_non_cross_pattern
from utils import parse_pattern, check_pattern


@pytest.mark.parametrize('s, pattern, expect_success', [
    ('ababababbcabcbcbce', 'x1_x1_a_b_x1_x2_a_b_c_x2_x2_e', True),
    ('aabcaababde', 'x1_a_b_c_x1_x2_x2_d_e', True),
    ('fffpepepepepepeosdosdosdosd', 'x1_x1_x1_x2_x2_x2_x2_x2_x2_x3_x3_x3_x3', True),
    ('ttbtnixrrtpnmssjssjmnfccmzmuoll', 'x1_x1_b_x1_x2_i_x_r_r_t_p_x2_m_x3_x3_x4_n_f_c_c_m_z_x4_u_o_l_l', True),
    ('ydnbpbtydgolwlwlwlwdsqdlgs', 'x1_n_b_p_b_t_x1_g_o_x2_x2_x2_x2_x3_s_q_x3_l_g_s', True),
    ('kfofdcaokfkfyywyywff', 'x1_o_f_d_c_a_o_x1_x1_x2_x2_x3_x3', True),
    ('ghghjshaghalttzttzbagjbbagjbagjbagj', 'x1_x1_j_s_h_a_x1_a_l_x2_x2_x3_b_x3_x3_x3', True),
    ('ststskckckckcgpfjgpfjdgpfjv', 'x1_t_s_t_x1_x2_x2_x2_x2_x3_x3_d_x3_v', True),
    ('xuujoyrxuueejvbeejvbeejvb', 'x1_j_o_y_r_x1_x2_x2_x2', True),
    ('ababababbcabcbcbce', 'x1_x1_a_b_x1_x2_a_b_c_x2_x2_e', True),
    ('aabcaababde', 'x1_a_b_c_x1_x2_x2_d_e', True),
    ('abcabcabcabcabcdeababaabab', 'a_b_c_x1_a_b_c_x1_x1_d_e_x2_x2_a_x2_x2', True),
    ('abababbcbcbce', 'x1_x1_x1_x2_x2_x2_e', True),
    ('aaaaaaaaabaabbe', 'x1_a_x1_a_x1_a_x2_a_a_x2_x2_e', True),
    ('aaaaaaaaabbaabbbbe', 'x1_a_x1_a_x1_a_x2_a_a_x2_x2_e', True),
    ('aaaaaaaaaabaabbe', 'x1_x1_x1_a_x1_a_a_a_a_a_x2_a_a_x2_x2_e', True),
    ('aaaaaaaaaaaae', 'x1_x1_x1_x2_x2_x2_e', True)
])
def test_non_cross_pattern(s: str, pattern: str, expect_success: bool):
    blocks = parse_pattern(pattern)
    matches = match_non_cross_pattern(s=s, blocks=blocks, matches={}, num_of_blocks=len(blocks))
    result = check_pattern(s=s, pattern=pattern, matches=matches)
    assert result == expect_success
