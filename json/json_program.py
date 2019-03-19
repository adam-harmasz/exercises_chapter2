import json
import re


def json_sum(filename):
    """Function to extract all numbers from the json file and sum them"""
    with open(filename, 'r') as f:
        # convert json data into string
        json_data = str(json.load(f))
        # regex to find all numbers with or without - in front of them
        regex = r'([0-9]+)|([-][0-9]+)'
        # list of all numbers
        my_list = [int(y) for x in re.findall(regex, json_data) for y in x if y != '']
        return sum(my_list)


print(json_sum('json_input.json'))
