def primes(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]

def is_prime(a):
    return all(a % i for i in xrange(2, a))

#all prime numbers less than 7000
prime_numbers = primes(50)

def is_sum_of_three_primes(num):
    prime_nums = []
    for i in prime_numbers:
        if i < num:
            prime_nums.append(i)
        else:
            break
    print 'prime nums  :',prime_nums
    result = False
    for i in range(len(prime_nums)-3):
        sum_of_three_primes = sum(prime_numbers[i:i+3])
        print sum_of_three_primes
        if sum_of_three_primes == num:
            result = True
            break
    print 'three primes  :',result
    return result

def main():
    for i in range(len(prime_numbers)-6):
        six_primes = prime_numbers[i:i+6]
        sum_of_six_primes = sum(six_primes)
        print i,six_primes,sum_of_six_primes
        if is_prime(sum_of_six_primes):
            print 'this is prime  :',sum_of_six_primes
            if is_sum_of_three_primes(sum_of_six_primes):
                print ' %d ' % sum_of_six_primes
                exit(0)

if __name__ == "__main__":
    main()
