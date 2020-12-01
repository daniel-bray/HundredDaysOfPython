# calculate whether the year is a leap year
# or not. if divisible by 4, then leap
# EXCEPT if divisible by 100 - not leap
# UNLESS also divisible by 400 - leap

year = int(input("Which year do you want to check? "))

is_leap = False

if year % 4 == 0:
    is_leap = True
if year % 100 == 0:
    is_leap = False
if year % 400 == 0:
    is_leap = True

if is_leap:
    print("Leap year")
else:
    print("Not a leap year")
