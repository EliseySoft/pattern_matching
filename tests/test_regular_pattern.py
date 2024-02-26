import pytest

from regular_patterns.match_regular_pattern import match_regular_pattern
from utils import check_pattern


@pytest.mark.parametrize('s, pattern, expect_success', [
    ('sdwrsmkghkfctpkntviborcresmeaq', 's_x1_h_x2_c_x3_x4_x5', True),
    ('pihqkjuykpvaddhzbtzfxwoeubcasxjexnflov', 'x1_h_q_k_j_x2_x3_x4_x5', True),
    ('waxqfkwitwnjeuqbsuxurrbfsddcjpgse', 'x1_x2_j_e_x3_x4_x5_x6', True),
    ('qeahixznyyckmnhfnqceavnfdbgfkljtz', 'q_x1_x2_n_x3_x4_x5_f_x6_x7', True),
    ('zoilktqaxugeimfdoqwkfytiqgxtuuvzhbcpbctk', 'x1_x2_x3_x4_x5', True),
    ('bpuuzsqicjduaifeppopcslmjkjpqzznudcuysjefl', 'b_p_x1_x2_x3_l_x4_u_x5', True),
    ('pwchahpfgnzdealczvocrkgvxchtoedampq', 'p_x1_x2_x3_x4_v_x5_x6_h_t_o_e_x7_x8', True),
    ('hmqsfmhevkvqgqovvmdzprrcpimzujkxxdwtj', 'x1_x2_x3_m_x4_x5_x6_x_x_d_w_x7', True),
    ('iwqywtxazeltomalkbvckvayfnabekkpaujpbk', 'x1_x_a_x2_x3_b_x4_x5_x6_k', True),
    ('qyowkzikojkfqtgctmulzkeyldutnbqkbmpnbxfgx', 'x1_o_w_k_x2_k_x3_x4_x5_x6_x7', True),
    ('zsmvaflxxysbrqknbmgfuygcfamxqqbyovszpfnxmpbnmih', 'x1_x_y_x2_x3_f_x4_m_x_q_x5_p_x6_n_x7', True),
    ('unkxxvsgjsorzvdwrbbzjkbqhxxctcsriamwvochc', 'x1_x2_x3_x4_b_q_h_x5_x6_x7_x8_x9_c', True),
    ('fvgetsmdvmugjxhpdlylrzgasqticzvnepbqjtypmxtqijwn', 'x1_x2_x3_x4_c_z_x5_t_x6', True),
    ('lqhsrabsdjemtvmebrwxezlzwaxvdcndeypcewemxqk', 'l_q_h_s_x1_a_b_s_d_x2_x3_x4_x5_x6_x7', True),
    ('gxgyoxcjwafsmgjemdvfpphaiqjuckykfwlwgxbbnquzgmdvzq', 'g_x1_x2_f_x3_c_k_x4_x5_x6_u_x7', True),
    ('xsltiadozvottnobjmbzigztdwyvptmlidjguqpoqiiuvpcde', 'x_x1_x2_x3_x4_j_m_x5_y_v_p_t_m_l_i_d_j_g_x6_q_x7_u_x8', True),
    ('uemvefhfoenwrreephluirzxgzihcqhcfntmwhxaalapsvpf', 'u_x1_o_e_n_w_x2_h_l_u_i_r_z_x_x3_x4_h_x5_x6', True),
    ('tbqzoutzjtobfziuofeqjyfexzgdqaaavfqvranpppezsjy', 't_x1_x2_x3_x4_x5_x6_y', True),
    ('bpxwjynhzcazbcptwnskvyvtheizkvbkocbrulrrabwsociwcso', 'b_p_x_w_x1_x2_b_x3_x4_z_k_x5_x6_x7', True),
    ('lypzmpqoqermpbcbacisvixtfekptjhjvawhpokxcktxdupglfqpfv', 'l_y_p_x1_x2_x3_j_h_j_v_x4_x5_d_u_p_x6', True)
])
def test_regular_pattern(s: str, pattern: str, expect_success: bool):
    _, matches = match_regular_pattern(word=s, pattern=pattern)
    result = check_pattern(s=s, pattern=pattern, matches=matches)
    assert result == expect_success
