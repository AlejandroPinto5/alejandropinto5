def get_pay(num_hours, hour_wage, rate_taxes):
    full_pay = num_hours*hour_wage
    house_pay= full_pay*(1-rate_taxes)
    return house_pay

total_pay = get_pay(48,6.25, .12)
print(total_pay)
