def raiz_cuadrada(y):
    L = 0
    M = 0
    R = y + 1

    while L != (R - 1):
        M = (L + R) >> 1
        if M * M <= y:
            L = M
        else:
            R = M
    return L


def es_primo(n: int) -> bool:
    n = int(n)
    if n < 2:
        return False
    if n == 2:
        return True

    for d in range(2, raiz_cuadrada(n) + 1):
        if n % d == 0:
            return False
    return True
