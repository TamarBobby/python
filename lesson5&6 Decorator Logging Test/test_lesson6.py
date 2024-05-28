import math

def find_primes(num):
    primes = []
    for i in range(1, num+1):
        is_prime = True
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes

print(find_primes(10))

def test_find_primes():
    assert find_primes(10) == [1,2, 3, 5, 7]
    assert find_primes(-10) == []
    assert find_primes(0) == []