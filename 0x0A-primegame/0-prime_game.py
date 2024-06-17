#!/usr/bin/python3
"""Prime Game"""


def isWinner(x, nums):
    """Determines the winner of a prime game session with `x` rounds.
    """
    if x < 1 or not nums:
        return None
    marias_wins, bens_wins = 0, 0
    k = max(nums)
    primes = [True for _ in range(1, k + 1, 1)]
    primes[0] = False
    for y, is_prime in enumerate(primes, 1):
        if y == 1 or not is_prime:
            continue
        for z in range(y + y, k + 1, y):
            primes[z - 1] = False
    for _, k in zip(range(x), nums):
        primes_count = len(list(filter(lambda x: x, primes[0: k])))
        bens_wins += primes_count % 2 == 0
        marias_wins += primes_count % 2 == 1
    if marias_wins == bens_wins:
        return None
    return 'Maria' if marias_wins > bens_wins else 'Ben'
