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
prime_numbers = primes(10000000)

def is_sum_of_primes(num, count):
    prime_nums = []
    for i in prime_numbers:
        if i < num:
            prime_nums.append(i)
        else:
            break
    result = False

    for i in xrange(len(prime_nums)-count):
        sum_of_primes = sum(prime_numbers[i:i+count])
        if sum_of_primes == num:
            print '%d primes  %s:' %(count, str(prime_numbers[i:i+count]))
            result = True
            break
    return result

def main():
    for i in xrange(len(prime_numbers)-541):
        sum_of_primes = sum(prime_numbers[i:i+541])
        if is_prime(sum_of_primes):
            if is_sum_of_primes(sum_of_primes, 41):
                if is_sum_of_primes(sum_of_primes, 17):
                    if is_sum_of_primes(sum_of_primes, 7):
                        print '541 primes   :',prime_numbers[i:i+541]
                        print 'This is the smallest sum %d ' % sum_of_primes
                        exit(0)
    print 'no result found'

if __name__ == "__main__":
    main()
