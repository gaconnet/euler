"""
You are given the following information, but you may prefer to do some
research for yourself.

* 1 Jan 1900 was a Monday.
* Thirty days has September,
  April, June and November.
  All the rest have thirty-one,
  Saving February alone,
  Which has twenty-eight, rain or shine.
  And on leap years, twenty-nine.
* A leap year occurs on any year evenly divisible by 4, but not on a century
  unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

"""


DAYS_IN_MONTH = (None, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
WEEKDAYS = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday',
            'Friday', 'Saturday')



def days_in_month(year, month):
    if month == 2:  # February; check for leap year
        divisible_by_4 = year % 4 == 0
        century = year % 100 == 0
        divisible_by_400 = year % 400 == 0

        if divisible_by_4 and not (century and not divisible_by_400):
            return 29

    return DAYS_IN_MONTH[month]



def first_of_months(start_year, start_month, start_dow):
    year = start_year
    month = start_month
    dow = start_dow
    weekday = WEEKDAYS[dow]

    while True:
        yield year, month, dow, weekday

        days = days_in_month(year, month)
        dow = (dow + days_in_month(year, month)) % 7
        weekday = WEEKDAYS[dow]

        month = (month % 12) + 1
        if month == 1:
            year += 1


if __name__ == '__main__':
    sunday_count = 0

    for y, m, dow, day in first_of_months(1900, 1, 1):
        if y > 2000:
            break

        if y > 1900 and day == 'Sunday':
            sunday_count += 1

    print sunday_count, "Sundays"
