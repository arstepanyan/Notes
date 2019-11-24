"""
Write a program that takes an integer argument and returns all the primes between 1 and that integer.
For example, if the input is 18, you should return [2,3,5,7,11,13,17].
A natural number is called a prime if it is bigger than 1 and has no divisors other than 1 and itself.
"""


# Time = O(n log log n) Explanation: The time to shift out the multiples of num is proportional to n/num,
#                                    so the overall time complexity is O(n/2 + n/3 + n/5 + n/7 + n/11 + ...).
#                                    It is not obvious but this sum asymptotically tends to (n log log n)
# Space = O(n)
def find_primes(n):
    primes = []
    is_prime = [False, False] + [True] * (n - 1)

    for num in range(2, n + 1):
        if is_prime[num]:
            primes.append(num)
            for i in range(num, n + 1, num):
                is_prime[i] = False
    return primes


if __name__ == "__main__":
    print(find_primes(18))
    print(find_primes(30))
