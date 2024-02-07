'''
    Implementation of a Linear Search. Big O worst case runtime is O(n) because we'd have to search the entire array/list to find the needle in the haystack. 
    The larger the haystack, the longer it's going to take
'''

from typing import List

def linear_search(haystack: List[int], needle: int) -> bool:
    for item in haystack:
        if item == needle:
            print(f"Needle: {needle} is in Haystack: {haystack}. True")
            return True

    print(f"Needle: {needle} is NOT in Haystack: {haystack}. False")
    return False
