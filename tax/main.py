from operator import mul

def slot1_tax(tax):
    #tax for first slot
    tax.append(tax[-1]+1)
    return tax


def slot2_tax(tax):
    #tax for second slot
    tax.append(tax[-1]*2)
    return tax

def print_tax(tax):
    print tax[-1]

def subseq_tax(tax,k):
    #subsequent years  18811834
    tax.append(reduce(mul, tax[-k:]) % 100000007)
    return tax

def calculate_tax(m):
    initTax,s1,s2,k,n = m
    tax = [initTax]
    for i in range(n-1):
        if len(tax) <= s1:
            tax = slot1_tax(tax)
        elif len(tax) <= s1+s2:
            tax = slot2_tax(tax)
        else:
            tax = subseq_tax(tax,k)
    print_tax(tax)

if __name__ == '__main__':
    tests = ((1,3,2,4,5),(1,3,2,4,7),(1,3,2,4,9))
    for test in tests:
        calculate_tax(test)

