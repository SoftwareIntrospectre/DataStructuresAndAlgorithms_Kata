'''
    Practice Linear Search in Python. Learn the gist in JavaScript from course, but translate it into Python
'''
from typing import List

def linear_search(haystack: List[int], needle: int) -> bool:
    for item in haystack:
        if item == needle:
            print(f"Needle: {needle} is in Haystack: {haystack}. True")
            return True

    print(f"Needle: {needle} is NOT in Haystack: {haystack}. False")
    return False
