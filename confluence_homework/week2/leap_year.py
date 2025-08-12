
year = int(input('Enter a year:'))

def check_leap_year(year):
    return (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)

if check_leap_year(year):
        print('This is a leap year')
else:
      print('This isnt a leap year')