'''
Simple demonstration of Sieve's algorithm
'''


def SieveOfEratosthenes(n):
    prime = [True for i in range(2, n+1)]
    p = 2

    while(p * p < n):
        if prime[p]:
            for i in range(p*p, (n+1), p):  # multiple of p that are >= p*p
                prime[i] = False

        p += 1

    for p in range(2, n+1):
        if prime[p]:
            print(p, end=', ')


n = int(input('Please enter the number: '))

SieveOfEratosthenes(n)
