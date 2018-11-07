def primes():
    a = 2
    while True:
        n = 0
        for i in range(1, a + 1):
            if a % i == 0:
                n += 1
        if n == 2:
            yield a
        a += 1

import itertools

print(list(itertools.takewhile(lambda x : x <= 31, primes())))
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]