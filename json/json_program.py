import json
import re


def json_sum(filename):
    """Function to extract all numbers from the json file and sum them"""
    with open(filename, 'r') as f:
        # convert json data into string
        json_data = str(json.load(f))
        # regex to find all numbers with or without - in front of them
        regex2 = r'[0-9]+|[-][0-9]+'
        # change type of numbers from string to integer so they can be summed
        my_list = [int(x) for x in re.findall(regex2, json_data)]
        return sum(my_list)


print(json_sum('json_input.json'))
