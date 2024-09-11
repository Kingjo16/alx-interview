#!/usr/bin/python3
"""Prime Game Logic Module."""


def isWinner(x, nums):
    """Evaluates who wins in a prime game session with specified rounds."""
    if x < 1 or not nums:
        return None
    maria_score, ben_score = 0, 0

    max_limit = max(nums)
    prime_flags = [True for _ in range(1, max_limit + 1, 1)]
    prime_flags[0] = False
    for index, is_prime in enumerate(prime_flags, 1):
        if index == 1 or not is_prime:
            continue
        for j in range(index + index, max_limit + 1, index):
            prime_flags[j - 1] = False

    for _, n in zip(range(x), nums):
        total_primes = len(list(filter(lambda x: x, prime_flags[0: n])))
        ben_score += total_primes % 2 == 0
        maria_score += total_primes % 2 == 1
    if maria_score == ben_score:
        return None
    return 'Maria' if maria_score > ben_score else 'Ben'
