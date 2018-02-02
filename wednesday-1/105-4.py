number_of_coins = 0
print('You have %s coins' % number_of_coins)
do_you_want_a_coin = raw_input('Do you want a coin?')
while do_you_want_a_coin == 'yes':
    number_of_coins += 1
    print('You have %s' % number_of_coins)
    do_you_want_a_coin = raw_input('Do you want another?')
print 'Bye'