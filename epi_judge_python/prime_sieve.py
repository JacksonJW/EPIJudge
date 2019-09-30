from test_framework import generic_test


# Given n, return all primes up to and including n.
def generate_primes(n):
    if n < 2:
        return []
    primes = []
    for num in range(2, n+1):
        if not primes:
            primes.append(num)
        else:
            prime_index = 0
            while True:
                if num % primes[prime_index] == 0:
                    break
                if prime_index == len(primes)-1:
                    primes.append(num)
                    break
                prime_index += 1
    return primes


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("prime_sieve.py", "prime_sieve.tsv",
                                       generate_primes))
