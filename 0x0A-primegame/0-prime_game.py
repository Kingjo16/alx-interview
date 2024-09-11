#!/usr/bin/python3
"""Prime Game Logic Module."""


def determine_winner(rounds_count, upper_limits):
    """Evaluates who wins in a prime game session with specified rounds."""
    if rounds_count < 1 or not upper_limits:
        return None
    maria_score, ben_score = 0, 0
    # Generate primes up to the maximum limit found in upper_limits
    max_limit = max(upper_limits)
    prime_flags = [True for _ in range(1, max_limit + 1)]
    prime_flags[0] = False
    for index, is_prime in enumerate(prime_flags, 1):
        if index == 1 or not is_prime:
            continue
        for multiple in range(index + index, max_limit + 1, index):
            prime_flags[multiple - 1] = False
    # Count primes less than each limit round
    for _, limit in zip(range(rounds_count), upper_limits):
        total_primes = len(list(filter(lambda x: x, prime_flags[0: limit])))
        ben_score += total_primes % 2 == 0
        maria_score += total_primes % 2 == 1
    if maria_score == ben_score:
        return None
    return 'Maria' if maria_score > ben_score else 'Ben'
