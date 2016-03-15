class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        if n < 3:
            return 0
        primes = [1]*n
        primes[0] = primes[1]  = 0
        for i in range(0,int(n**0.5)+1):
            if primes[i] != 0:
                primes[i*i:n:i] = [0]*len(primes[i*i:n:i])
        return sum(primes)