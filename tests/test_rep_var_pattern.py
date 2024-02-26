import pytest

from rep_var_patterns.match_rep_var_pattern import match_rep_var_pattern
from utils import check_pattern


@pytest.mark.parametrize('s, pattern, expect_success', [
    ('zuiinzuviikzuzutiiciibb', 'x2_x3_n_x2_x4_x3_k_x2_x2_x5_x3_x6_x3_x1_x1', True),
    ('tfhaajfgffajhgchaajf', 't_x2_x1_x3_x2_g_x2_x2_x3_x4_c_x1_x3_x2', True),
    ('ppoupoupzzppousezfou', 'x3_x3_x2_x3_x2_x3_z_x1_x3_x3_x2_s_e_x1_f_x2', True),
    ('opibgiibibibibycwicibuuwi', 'x4_x1_x5_x1_x1_x1_x1_x6_x3_x7_x1_x2_x2_x3', True),
    ('xwsxwbawnytxwyyleyjzwn', 'x2_x4_x2_x5_x3_x1_t_x2_x1_x1_x6_e_x1_x7_x3', True),
    ('mhegtjswegymsoegplhmpe', 'x4_h_x3_x5_j_x6_x2_y_x7_o_x2_x1_x8_x9_x10_x1_x3', True),
    ('hhkrmlzkrkrenmkrkren', 'x4_x1_x2_l_x5_x1_x1_x3_x2_x1_x1_x3', True),
    ('drkrkfezrkzrkzxrkprgr', 'x4_x2_x2_x5_x6_x1_x2_x1_x2_x1_x_x7_p_x3_g_x3', True),
    ('nonnhpvvxgxzsgtndnvv', 'x1_x4_x1_x1_x5_x2_x3_x6_x3_z_x7_t_x1_d_x1_x2', True),
    ('xuaerxxxeeepvpvepvxe', 'x1_u_a_x3_r_x1_x_x1_x3_x3_x3_x2_x2_x3_x2_x1_x3', True),
    ('drlrfbtjjlrjtmtlrtlr', 'x4_x1_f_b_x2_x3_x5_x1_x3_x2_m_x6_x1_x2_x1', True),
    ('oupfuputupuppzrupnupof', 'x1_x2_x3_x2_x4_x2_x2_x5_x6_r_x2_n_x2_x1_x3', True),
    ('qnqqnbqnqnkmeqnehboqn', 'x3_q_x3_x1_x3_x3_k_m_x2_x3_x2_x4_x1_x5_x3', True),
    ('dnsofsofddnssofofadn', 'x1_s_x3_x2_x3_d_x1_x2_x2_x3_x3_a_x1', True),
    ('ocoryookrzdnoootkrvono', 'x3_c_x3_x1_x4_x3_x3_k_x1_x5_x2_x3_x3_x6_x1_x7_x3_x2', True),
    ('znijwleugvmznijwleumg', 'x2_x1_x3_v_x4_x2_x1_m_x3', True),
    ('zpbpewypvvallbzxapvszpbpewy', 'x2_x3_x1_x4_x5_x6_x1_s_x2_x3', True),
    ('etetdwbdwbdwbuggetkysukysu', 'x2_x2_x3_x3_x3_x4_g_x2_x1_x1', True),
    ('iotbhjxbiouiiwhbcyubcyu', 'x3_t_x2_x4_x_x2_x3_x5_w_h_x2_x1_x2_x1', True),
    ('vjkjxabrpxabrpjmoxsqxdlptxdlptaiddaidd', 'x4_x3_x3_x5_q_x1_x1_x2_x2', True)
])
def test_rep_var_pattern(s: str, pattern: str, expect_success: bool):
    matches = match_rep_var_pattern(s=s, pattern=pattern)
    result = check_pattern(s=s, pattern=pattern, matches=matches)
    assert result == expect_success
