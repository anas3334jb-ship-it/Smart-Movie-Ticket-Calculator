standard_price = 12
age_str = input('Enter your Age:')
if age_str.isdigit() or (age_str.startswith('-') and age_str[1:].isdigit()):
    Age = int(age_str)
else:
    print('Invalid input! Please enter a valid whole number.')
    exit()
if Age < 0 :
    print('Invalid Age')
    exit()
onweek_day = (input('It is Week Day or Not(True or False):'))
if onweek_day != 'True' and onweek_day !='False':
    print('Invalid input')
    exit()
if Age <= 12 :
    process = standard_price*(50/100)
    discount = standard_price - process
    if onweek_day == 'False':
        print('You got 50% Discount and you have to pay:',discount)       
    elif onweek_day == 'True':
        final_price = discount - 2
        print('Week Day offer you have to pay:',final_price)
elif Age >= 65:
    process = standard_price*(30/100)
    discount = standard_price - process
    if onweek_day == 'False':
        print('You got 30% Discount and you have to pay:',discount) 
    elif onweek_day == 'True': 
        final_price = discount - 2
        print('Week Day offer you have to pay:',final_price)
elif Age < 65 and Age >12:
    student = input('Student or not:')
    if student != 'student' and student != 'not':
        print('Invalid input')
        exit()
    process = standard_price*(20/100)
    discount = standard_price - process
    if student == 'student' and onweek_day == 'False':
        print('you got student discount:',discount)
    elif student == 'student' and onweek_day == 'True':
        final_price = discount - 2
        print('Week Day offer you have to pay:',final_price)
    else:
        if onweek_day == 'True':
            final_price = standard_price - 2
            print('Week Day offer you have to pay:',final_price)
        elif onweek_day == 'False': 
            print('You have to pay:',standard_price)
else:
    print('You have to pay:',standard_price)
