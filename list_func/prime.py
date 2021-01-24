def is_prime(n: int) -> bool:
    if n <= 1:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return True

    i = 3

    while i * i <= n:
        if n % i == 0:
            return False

        i += 2

    return True