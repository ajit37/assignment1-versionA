#!/usr/bin/env python3

'''
OPS435 Assignment 1 - Summer 2023
Program: assignment1.py 
Author: Ajit Virk
The python code in this file (a1_avirk18.py) is original work written by
Ajit Virk. No code in this file is copied from any other source
except those provided by the course instructor, including any person,
textbook, or on-line resource. I have not shared this python script
with anyone or anything except for submission for grading. I understand
that the Academic Honesty Policy will be enforced and
violators will be reported and appropriate action will be taken.
'''

import sys

def day_of_week(year: int, month: int, date: int) -> str:
    "Based on the algorithm by Tomohiko Sakamoto"
    days = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat'] 
    offset = {1:0, 2:3, 3:2, 4:5, 5:0, 6:3, 7:5, 8:1, 9:4, 10:6, 11:2, 12:4}
    if month < 3:
        year -= 1
    num = (year + year//4 - year//100 + year//400 + offset[month] + date) % 7
    return days[num]


def mon_max(month:int, year:int) -> int:
    "returns the maximum day for a given month. Includes leap year check"
    if month == 2:
    #Using the leap year rule in the if statement to determin leap year
        if leap_year(year):
            return 29 
        else:
            return 28
    elif month in [4,6,9,11]:
        return 30 
    else:
        return 31

def after(date: str) -> str:
    '''
    after() -> date for next day in YYYY-MM-DD string format

    Return the date for the next day of the given date in YYYY-MM-DD format.
    This function takes care of the number of days in February for leap year.
    This fucntion has been tested to work for year after 1582
    '''
    str_year, str_month, str_day = date.split('-')
    year = int(str_year)
    month = int(str_month)
    day = int(str_day)
    tmp_day = day + 1  # next day

    if tmp_day > mon_max(month, year):
        to_day = tmp_day % mon_max(month, year)  # if tmp_day > this month's max, reset to 1 
        tmp_month = month + 1
    else:
        to_day = tmp_day
        tmp_month = month + 0

    if tmp_month > 12:
        to_month = 1
        year = year + 1
    else:
        to_month = tmp_month + 0

    next_date = f"{year}-{to_month:02}-{to_day:02}"

    return next_date


def usage():
    "Print a usage message to the user"
    ...


def leap_year(year: int) -> bool:
    return (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))
    "return True if the year is a leap year"
    ...

def valid_date(date: str) -> bool:
    "check validity of date and return True if valid"

    # Step 1: Check if the date is in the correct format (YYYY-MM-DD)
    if len(date) != 10:
        return False
    if date[4] != '-' or date[7] != '-':
        return False

    # Step 2: Split the date into year, month, and day
    try:
        year = int(date[:4])
        month = int(date[5:7])
        day = int(date[8:])
    except ValueError:
        return False  # If conversion to integer fails, it's an invalid date

    # Step 3: Check if the month is valid (1-12)
    if not (1 <= month <= 12):
        return False

    # Step 4: Check if the day is valid based on the month and year
    # Days in each month for non-leap years
    days_in_month = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }

    # Adjust February days for leap years
    if leap_year(year):
        days_in_month[2] = 29

    # Step 5: Check if the day is valid for the given month
    if not (1 <= day <= days_in_month[month]):
        return False

    # If all checks pass, the date is valid
    return True

def day_count(start_date: str, stop_date: str) -> int:
#    "Loops through range of dates, and returns number of weekend days"
      
    if not valid_date(start_date) or not valid_date(stop_date):
        raise ValueError("Invalid date format. Use YYYY-MM-DD.")
    
    weekend_count = 0
    current_date = start_date

    # Loop until the current date is the stop date
    while current_date <= stop_date:
        year, month, day = map(int, current_date.split('-'))
        weekday = day_of_week(year, month, day)
        
        # Check if the day is a weekend (Saturday or Sunday)
        if weekday == 'sun' or weekday == 'sat':
            weekend_count += 1

        # Move to the next day
        current_date = after(current_date)

    return weekend_count


if __name__ == "__main__":
    ...
