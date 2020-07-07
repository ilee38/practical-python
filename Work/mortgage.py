# mortgage.py
#
# Exercise 1.7
# mortgage.py

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    month += 1
    extra_pay = 0
    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        extra_pay = extra_payment
    if payment >= principal * (1+rate/12):
        payment = principal * (1+rate/12)
        extra_pay = 0
    principal = principal * (1+rate/12) - (payment + extra_pay)
    total_paid = total_paid + (payment + extra_pay)
    print(month, round(total_paid, 2), round(principal, 2))
    

print('Total paid', round(total_paid, 2))
print('Over ', month, ' months')