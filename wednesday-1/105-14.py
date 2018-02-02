countdown = int(raw_input('Where should we start?'))
while countdown > 20:
    countdown = int(raw_input('sorry - got to put a number lower than 20.'))

while countdown >= 0:
    print countdown
    countdown -= 1

if countdown < 0:
    print 'blast off!'