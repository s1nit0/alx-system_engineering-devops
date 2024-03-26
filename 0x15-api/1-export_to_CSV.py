#!/usr/bin/python3

# Script for exporting JSON data to CSV
""" used moduls"""
import csv
from requests import get
from sys import argv


# export function
def cvsWrite(user):
    """Fetches data from a JSON API and exports it to a CSV file.

    Args:
        user (int): The user ID for which data is to be fetched.

    function retrieve data for a specific user from a JSON API to a CSV file.
    The data includes user-specific information and todo items.

    Example:
        cvsWrite(1)  # Fetches data for user ID 1 and exports it to a CSV file.
    """
    data = get('https://jsonplaceholder.typicode.com/todos?userId={}'.format(
        user)).json()
    name = get('https://jsonplaceholder.typicode.com/users/{}'.format(
        user)).json().get('username')
    employ_data = open('{}.csv'.format(user), 'w')
    cwrite = csv.writer(employ_data, quoting=csv.QUOTE_ALL)
    for line in data:
        lined = [line.get('userId'), name,
                 line.get('completed'), line.get('title')]
        cwrite.writerow(lined)
    employ_data.close()


if __name__ == "__main__":
    cvsWrite(argv[1])
