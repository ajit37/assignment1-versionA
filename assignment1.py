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
    # Based on the algorithm by Tomohiko Sakamoto
    days = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat'] 
    offset = {1:0, 2:3, 3:2, 4:5, 5:0, 6:3, 7:5, 8:1, 9:4, 10:6, 11:2, 12:4}
    if month < 3:
        year -= 1
    num = (year + year//4 - year//100 + year//400 + offset[month] + date) % 7
    return days[num]


def mon_max(month:int, year:int) -> int:
    # Returns the maximum day for a given month. Includes leap year check
    if month == 2:
    # Using the leap year rule in the if statement to determine leap year
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
    # Print a usage message to the user
    print("Usage: python assignment1.py <start_date> <end_date>")
    print("Where <start_date> and <end_date> are in the format 'YYYY-MM-DD'.")
    print("Example: python assignment1.py 2023-03-27 2023-05-28")
    print("\nBoth dates must be valid and the start date must be earlier than the end date.")
    sys.exit(1)

def leap_year(year: int) -> bool:
    if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
        return True
    #Return True if the year is a leap year"

def valid_date(date: str) -> bool:
    '''
    Check validity of date in YYYY-MM-DD format and return True if valid.
    '''
    # Normalize the date format to ensure it's in the form 'YYYY-MM-DD'
    normalized_date = normalize_date_format(date)

    if normalized_date is None:
        return False  # Invalid date format after normalization
    
    year, month, day = map(int, normalized_date.split('-'))
    if not (1 <= month <= 12):
        return False  # Invalid month
    
    days_in_month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
                     7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    if leap_year(year):
        days_in_month[2] = 29  # Adjust February days for leap years

    if not (1 <= day <= days_in_month[month]):
        return False  # Invalid day
    return True


def normalize_date_format(date: str) -> str:
    """
    Normalize a date string of the form 'YYYY-M-D' or 'YYYY-MM-DD' to 'YYYY-MM-DD'.
    Returns the normalized date if valid, otherwise None.
    """
    parts = date.split('-')
    
    # Check if the date is in a valid format (either YYYY-M-D or YYYY-MM-DD)
    if len(parts) != 3:
        return None
    
    # Normalize month and day to always be two digits
    year, month, day = parts
    
    # Ensure the year is four digits
    if len(year) != 4 or not year.isdigit():
        return None
    
    # Ensure month and day are numeric
    if not (month.isdigit() and day.isdigit()):
        return None
    
    # Normalize month and day to two digits
    month = month.zfill(2)
    day = day.zfill(2)
    
    # Return the normalized date string
    return f"{year}-{month}-{day}"


def check_date_order(start_date: str, stop_date: str) -> bool:
    '''
    Ensure that the start date is earlier than the stop date.
    If not, raise a ValueError.
    '''
    # Normalize both dates
    start_date_normalized = normalize_date_format(start_date)
    stop_date_normalized = normalize_date_format(stop_date)

    # If either date is invalid, raise an error
    if not start_date_normalized or not stop_date_normalized:
        raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'.")

    # If the start date is later than the stop date, swap them
    if start_date_normalized > stop_date_normalized:
        start_date_normalized, stop_date_normalized = stop_date_normalized, start_date_normalized

    return start_date_normalized, stop_date_normalized

def day_count(start_date: str, stop_date: str) -> int:
    '''
    Loops through range of dates, and returns number of weekend days (Saturdays and Sundays). 
    This also normalizes and validates the date order to ensure the start date is earlier than the end.
    '''
    # Check and correct date order andn swap if needed
    start_date, stop_date = check_date_order(start_date, stop_date)

    weekend_count = 0
    current_date = start_date

    while current_date <= stop_date:
        year, month, day = map(int, current_date.split('-'))
        weekday = day_of_week(year, month, day)

        # Check if the day is a weekend (Saturday or Sunday)
        if weekday == 'sun' or weekday == 'sat':
            weekend_count += 1
        
        # Move to the next day
        current_date = after(current_date)

    return print(f"The period between {start_date} and {stop_date} includes {weekend_count} weekend days.")


if __name__ == "__main__":
    # Check if we have two arguments, start_date and stop_date
    if len(sys.argv) != 3:
        print("Error: You must provide exactly two date arguments.")
        usage()
        sys.exit(1)
    
    start_date = sys.argv[1]
    stop_date = sys.argv[2]
    
    # Validate both dates
    if not valid_date(start_date):
        print(f"Error: The start date '{start_date}' is not valid.")
        usage()
    
    if not valid_date(stop_date):
        print(f"Error: The stop date '{stop_date}' is not valid.")
        usage()

    # Calculate the number of weekends
    try:
        weekend_days = day_count(start_date, stop_date)
        print(f"The period between {start_date} and {stop_date} includes {weekend_days} weekend days.")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
