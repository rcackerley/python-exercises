number = int(raw_input('Number?'))

if number % 2 == 0:
    i = 1
    while i < number:
        if (number % i) == 0:
            factor = number / i
            print '%s,%s' % (factor, i)
            i += 1


else:
    print '1,%s' % number