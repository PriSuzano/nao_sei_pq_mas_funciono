import math, itertools
import operator
import functools

n = int(input())

def divisors(num):
    for i in range(1, num//2+1):
        if num % i == 0 and isPrime(i):
            yield i

def isPrime(n):
        start = 2;
        while start <= math.sqrt(n):
            if n % start < 1:
                return False;
            start += 1;
        return n > 1;

divisores = list(divisors(n))

despojados = 0
for i in range(1, len(divisores)+1):
    comb = list(itertools.combinations(divisores, i))
    for elem in comb:
        if functools.reduce(operator.mul, elem, 1) == n:
            despojados+=1

print('despojados', despojados)
print('divisores', divisores)