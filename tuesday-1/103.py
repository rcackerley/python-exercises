#Excercise for what day of the week
day = int(raw_input('Day (0-6)? '))

if day == 0:
    print 'Sunday'
elif day == 1:
    print 'Monday'
elif day == 2:
    print 'Tuesday'
elif day == 3:
    print 'Wednesday'
elif day == 4:
    print 'Thursday'
elif day == 5:
    print 'Friday'
elif day == 6:
    print 'Saturday'
else:
    print 'Not a valid day'

#Excercise to discover if it is the weekend or not
if day == 0 or day == 6:
    print 'Sleep in'
else:
    print 'go to work'

#Excercise to convert temp
temperature = float(raw_input('What\'s the temperature in Celsius?'))
f_temp = (temperature * 1.8) + 32.0

print f_temp

#Excercise to calculate Bill
total_bill_amount = float(raw_input('What\'s your bill amount? '))
level_of_service = raw_input('Was the service good, bad, or fair?')
split_times = float(raw_input('Split how many ways?'))
tip_percentage = 0.0

if level_of_service == 'good':
    tip_percentage = .20
elif level_of_service == 'fair':
    tip_percentage = .15
elif level_of_service == 'bad':
    tip_percentage = .10

tip = total_bill_amount * tip_percentage

what_you_pay = total_bill_amount + tip
amount_per_person = what_you_pay / split_times
print 'Tip Amount: %.2f' % (tip)
print 'Total Amount: %.2f' % (what_you_pay)
print 'Amount per persion: %.2f' % (amount_per_person)
