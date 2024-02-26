import pytest

from one_var_patterns.match_one_var_pattern import match_one_var_pattern
from utils import check_pattern


@pytest.mark.parametrize('s, pattern, expect_success', [
    ('hcflnqhcflnqmhcflnqc', 'x1_x1_m_x1_c', True),
    ('jehacgmsvkehacgmsvkmx', 'j_x1_x1_m_x', True),
    ('kgdnnzfavjkgdnnzfavjkgdnnzfavj', 'x1_x1_x1', True),
    ('adwzjqtlgkfmuxgadwzjwadwzj', 'x1_q_t_l_g_k_f_m_u_x_g_x1_w_x1', True),
    ('wiqkyfbwlgisfbwlgishjfbwlgis', 'w_i_q_k_y_x1_x1_h_j_x1', True),
    ('hhxyjybkplerhhxyjybkhxyjybk', 'h_x1_p_l_e_r_h_x1_x1', True),
    ('hivcbtmqvcbqhevcbkyoavcbavcb', 'h_i_x1_t_m_q_x1_q_h_e_x1_k_y_o_a_x1_a_x1', True),
    ('ffifwuwffzfffffojxffnffeffg', 'x1_i_f_w_u_w_x1_z_f_x1_x1_o_j_x_x1_n_x1_e_x1_g', True),
    ('ptavqathyrlinmsdavqathyravqathyr', 'p_t_x1_l_i_n_m_s_d_x1_x1', True),
    ('vtltxucqlhxucqlzxucqlixucqlxucql', 'v_t_l_t_x1_h_x1_z_x1_i_x1_x1', True),
    ('mogmmomjbkdwzegcybcmnjkelrmpev', 'x1_o_g_x1_x1_o_x1_j_b_k_d_w_z_e_g_c_y_b_c_x1_n_j_k_e_l_r_m_p_e_v', True),
    ('mxnxxnkxnaxnfxndqxnvxnxnxnaxnxn', 'm_x1_x_x1_k_x1_a_x1_f_x1_d_q_x1_v_x1_x1_x1_a_x1_x1', True),
    ('mazlwuazlwuqazlwurgazlwuvgeazlwu', 'm_x1_x1_q_x1_r_g_x1_v_g_e_x1', True),
    ('bjcgycgycgyafhtcgywlcgyyvmccgybnq', 'b_j_x1_x1_x1_a_f_h_t_x1_w_l_x1_y_v_m_c_x1_b_n_q', True),
    ('cfdvwbpqnzudvwdvoszcqpdvdvdvfkexdv', 'c_f_x1_w_b_p_q_n_z_u_x1_w_x1_o_s_z_c_q_p_x1_x1_x1_f_k_e_x_x1', True),
    ('sjqjnibymdosbinibymdosbinibymdosbib', 's_j_q_j_x1_x1_x1_b', True),
    (
            'yqnhhpokbrjlpppjppphwppgmvgglpwsujpd',
            'y_q_n_h_h_p_o_k_b_r_j_l_x1_x1_x1_j_x1_x1_x1_h_w_x1_x1_g_m_v_g_g_l_p_w_s_u_j_x1_d',
            True
    ),
    ('ypryywehhzfqjzhzfqhzfqhzfqhzfqnhzfqhzfq', 'y_p_r_y_y_w_e_h_x1_j_z_x1_x1_x1_x1_n_x1_x1', True),
    ('wjegdhhfegdhhmhsxegdhhggyegdhhegdhhuhegdhh', 'w_j_x1_f_x1_m_h_s_x_x1_g_g_y_x1_x1_u_h_x1', True),
    ('ximkwximcximbkeaximbtximecwximsaximyxim', 'x1_k_w_x1_c_x1_b_k_e_a_x1_b_t_x1_e_c_w_x1_s_a_x1_y_x1', True)
])
def test_one_var_pattern(s: str, pattern: str, expect_success: bool):
    _, matches = match_one_var_pattern(word=s, pattern=pattern)
    result = check_pattern(s=s, pattern=pattern, matches=matches)
    assert result == True
