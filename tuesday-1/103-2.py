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
tip = round(tip, 2)
what_you_pay = total_bill_amount + tip
amount_per_person = what_you_pay / split_times
print 'Tip Amount: ' + str(tip)
print 'Total Amount: ' + str(what_you_pay)
print 'Amount per persion: ' + str(amount_per_person)