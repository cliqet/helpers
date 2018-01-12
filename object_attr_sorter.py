"""Sorts a list of objects based on attribute specified"""

from operator import attrgetter

"""
    First parameter takes list of object
    Second parameter takes the String type attribute for basis of sorting
    Third paramter (optional) takes boolean value whether list should be sorted ascending or descending
    Return value is the sorted list
"""
def sort_object_list(obj_list, attr, desc=False):

    new_list = sorted(obj_list, key=attrgetter(attr), reverse=desc)
    return new_list



