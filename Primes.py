import this


class Primes():
    '''
    Created by Kyle Bomeisl 1/2/2024
    '''
    primes_list=[]

    def is_prime(self, number):
        '''
        Determines if a number is prime or not. If the number is prime
        then it is stored in :primes_list and true is returned. Otherwise false is returned

        :param number:
        :return boolean: false if number is not prime, true if number is prime
        '''
        if number <= 1:
            return False
        elif number in self.primes_list:
            return True
        else:
            return self.prime_test(number)

    def prime_test(self, number):
        '''
        Mathematically tests if a number is prime

        :param number:
        :return boolean: false if number is not prime, true if
        '''
        for n in range(2,number):
            if number % n != 0:
                return False
            else:
                return True

    def reverse_number(self, number):
        return int(reversed(str(number)))




