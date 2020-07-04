'''
Problem 5

Write a function

you get the leap year rules. There are 3 rules.

1. The year must be evenly divisible by 4
2. If the year can also be evenly divided by 100. It is not a leap year
3. The year is also evenly divisible by 400. Then is is a leap year
'''

def is_leap(year):
    if (( year%400 == 0) or (( year%4 == 0 ) and ( year%100 != 0))):
        leap=True
    else:
        leap=False
    return leap
year = int(input())
print(is_leap(year))