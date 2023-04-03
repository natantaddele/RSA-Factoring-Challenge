import sys


def factorize(n):
    """
    Returns a tuple (p, q) where p and q are two factors of n such that p*q = n.
    """
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return i, n // i
    return None


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: factors <file>')
        sys.exit(1)

    with open(sys.argv[1], 'r') as f:
        for line in f:
            n = int(line.strip())
            factors = factorize(n)
            if factors:
                print('{}={}*{}'.format(n, factors[0], factors[1]))
