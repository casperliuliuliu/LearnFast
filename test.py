import random

def pick_random(number_list: list=[], num: int=5)->list:
    # Check if the list has at least 5 unique elements
    if len(number_list) >= num:
        # Pick 5 random non-repeating numbers from the list
        return random.sample(number_list, num)
    else:
        print("The list doesn't have enough unique elements.")
        return []