from calendar import month, week


age = int(input("What is your corrent age? "))
age_max=70
y_age_left=age_max-age

year=y_age_left
month=year*12
week=month*4
day=week*7

print(f"You have {day} days, {week} weeks, {month} months, and {year} years left.")
