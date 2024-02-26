def z_function(s):
    n = len(s)
    z = [0] * n
    l, r = 0, 0
    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l = i
            r = i + z[i] - 1
    return z


def get_z(z, i):
    if 0 <= i < len(z):
        return z[i]
    else:
        return 0


def convert_to_repetitions(repetitions, shift, left, cntr, l, k1, k2):
    for l1 in range(max(1, l - k2), min(l, k1) + 1):
        if left and l1 == l:
            break
        l2 = l - l1
        pos = shift + (cntr - l1 if left else cntr - l - l1 + 1)
        repetitions.append((pos, pos + 2 * l - 1))


def find_xx_repetitions(s, shift=0, repetitions=None):
    if repetitions is None:
        repetitions = [(-1, -1)]  # повторение для пустой переменной

    n = len(s)
    if n <= 1:
        return repetitions

    nu = n // 2
    nv = n - nu
    u = s[:nu]
    v = s[nu:]
    ru = u[::-1]
    rv = v[::-1]

    repetitions = find_xx_repetitions(u, shift, repetitions)
    repetitions = find_xx_repetitions(v, shift + nu, repetitions)

    z1 = z_function(ru)
    z2 = z_function(v + '#' + u)
    z3 = z_function(ru + '#' + rv)
    z4 = z_function(v)

    for cntr in range(n):
        if cntr < nu:
            l = nu - cntr
            k1 = get_z(z1, nu - cntr)
            k2 = get_z(z2, nv + 1 + cntr)
        else:
            l = cntr - nu + 1
            k1 = get_z(z3, nu + 1 + nv - 1 - (cntr - nu))
            k2 = get_z(z4, (cntr - nu) + 1)
        if k1 + k2 >= l:
            convert_to_repetitions(repetitions, shift, cntr < nu, cntr, l, k1, k2)

    return repetitions
