import datetime
import json
from random import random
from datetime import datetime
from dateutil.parser import parse
from faker import Faker

fake = Faker()


# fake.date_between(start_date='today', end_date='+30d')
# fake.date_time_between(start_date='-30d', end_date='now')
#
# # Or if you need a more specific date boundaries, provide the start
# # and end dates explicitly.
# start_date = datetime.date(year=2015, month=1, day=1)
# fake.date_between(start_date=start_date, end_date='+30y')

def get_random_date():
    """Generate a random datetime between `start` and `end`"""
    return fake.date_time_between(start_date='-30d', end_date='now')


def get_random_date_in(start, end):
    """Generate a random datetime between `start` and `end`"""
    return start + datetime.timedelta(
        # Get a random amount of seconds between `start` and `end`
        seconds=random.randint(0, int((end - start).total_seconds())), )


def load_json_file(path):
    """Load JSON content from file in 'path'

    Parameters:
    path (string): the file path

    Returns:
    JSON: a JSON object
    """
    # Load the file into a unique string
    with open(path,encoding='utf-8') as fp:
        lines = fp.readlines()
    json_string = '['+','.join(lines) +  ']'
    # Parse the string into a JSON object
    json_data = json.loads(json_string)
    return json_data


def format_date(date):
    date = str(date)
    nums = date.split('-')
    year = nums[0]
    month = nums[1]
    match month:
        case "01": 
            month_name = "Jan"
        case "02": 
            month_name = "Feb"
        case "03": 
            month_name = "Mar"
        case "04": 
            month_name = "Apr"
        case "05": 
            month_name = "May"
        case "06": 
            month_name = "Jun"
        case "07": 
            month_name = "Jul"
        case "08": 
            month_name = "Aug"
        case "09": 
            month_name = "Sep"
        case "10": 
            month_name = "Oct"
        case "11": 
            month_name = "Nov"
        case "12": 
            month_name = "Dec"
        case _:
            month_name = ""
    day = nums[2][0:2]
    suffix = "th" if 11 <= int(day) <= 13 else {1: "st", 2: "nd", 3: "rd"}.get(int(day) % 10, "th")
    formatted_date = day + suffix + " " + month_name + " " + year
    return formatted_date
