n = input('Please insert number: ')
n = int(n)
counter = 0


class Prime():
    def __init__(self, n):
        self.n = n
        self.counter = 0
        self.sum_for_3 = 0
        self.primes = []
        self.prime_list = [2]
    def isPrime(self, n):
        if self.counter == 0:

            if str(n)[-1] == '0' or str(n)[-1] == '5':
                if self.counter == 0:
                    return (False, n, 'it is divisible by 5')

        max_value = n / 2
        while self.counter < len(self.prime_list):
            current_prime = self.prime_list[self.counter]
            if n % current_prime == 0:
                return (False, n)
            if self.prime_list[-1] >= max_value:
                return (True, n)
            if current_prime == self.prime_list[-1]:
                next_prime = current_prime + 1
                isNextPrime, next_prime = self.isPrime(next_prime)
                if isNextPrime:
                    self.prime_list.append(next_prime)
            self.counter += 1
    
    def checkInRange(self):
        for i in range(0, self.n):
            self.counter = 0
            self.primes.append(self.isPrime(i))
            
        return self.primes


prime = Prime(n)
#run this to check one number

print(prime.isPrime(n))
print(f'this took {prime.counter} steps')

# run this to check all numbers in a range
#print(prime.checkInRange())