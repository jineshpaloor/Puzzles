
def float_list_gen(start,end,step):
    r = start
    while r < end:
        r = float(str(r)[:str(r).find('.')+3])
        yield r
        r += step

def main():
    numbers = [(a,b,c,d) for a in float_list_gen(3.01,3.50, 0.01)
                         for b in float_list_gen(1.01, 1.51, 0.01)
                         for c in float_list_gen(1.01, 1.51, 0.01)
                         for d in float_list_gen(1.01, 1.51, 0.01)
                         if a+b+c+d == a*b*c*d == 7.11
            ]
    if numbers:
        print "The prices are  ",numbers[0]
    else:
        print 'No results found'

if __name__ == '__main__':
    main()
