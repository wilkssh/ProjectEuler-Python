import math


def is_prime(n: int) -> bool:
    """Primality test using 6k+-1 optimization."""
    if n <= 3:
        return n > 1
    if not n%2 or not n%3:
        return False
    i = 5
    stop = int(n**0.5)
    while i <= stop:
        if not n%i or not n%(i + 2):
            return False
        i += 6
    return True

def largest_prime_factor(val):
    largest = -1

    for num in range(math.ceil(math.sqrt(val))):
        if is_prime(num) and val % num == 0:
            largest = num
            print(f"num is {num}")

    return largest

if __name__ == "__main__":
    print(largest_prime_factor(600851475143))