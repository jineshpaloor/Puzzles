
def powers_of_two_less_than_hundred():
    return [pow(2,x) for x in range(1,7)]

def numbers_less_than_hundred():
    return [x for x in range(2,101)]

def get_odd_divisors(n):
    divisors = []
    for i in range(2, int(n/2)+1):
        if n%i == 0 and i%2 != 0:
            divisors.append(i)
    if n % 2 == 0:
        return divisors
    else:
        divisors.append(n)
        return divisors

def polite_numbers_less_than_hundred():
     return list(set(numbers_less_than_hundred()) - set(powers_of_two_less_than_hundred()))

def get_politeness():
    return [len(get_odd_divisors(x)) for x in polite_numbers_less_than_hundred()]

def get_number_with_highest_politenes():
    politeness_list = get_politeness()
    polite_list = polite_numbers_less_than_hundred()

    politeness_zip = zip(polite_list, politeness_list)

#    ind = polite_list.index(max(polite_list))
    max_polite = max(politeness_list)

    max_polite_numbers = []
    for i,j in politeness_zip:
        if j== max_polite:
            max_polite_numbers.append(i)
    return max_polite_numbers

if __name__ == '__main__':
    print '*'*50
    print 'Polite numbers less than hundred'
    print '*'*50
    print polite_numbers_less_than_hundred()
    print '*'*50
    print 'Numbers with highest politeness'
    print '*'*50
    print get_number_with_highest_politenes()

