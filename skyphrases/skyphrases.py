from skyphrase_input import puzzle_input


test_input = """aa bb cc dd ee
aa bb cc dd aa
aa bb cc dd aaa"""


def check_skyphrase(input_list):
    """Function to check number of valid skyphrases"""
    # puzzle input splitted into list of lists
    split_input = [phrase.split(' ') for phrase in input_list.splitlines()]
    # check if lenth of phrase is equal to length of set, if not it means that some word
    # was duplicated, and return number of valid phrases
    return len([phrase for phrase in split_input if len(phrase) == len(set(phrase))])


print(check_skyphrase(test_input))
print(check_skyphrase(puzzle_input))