from typing import List

def linear_search(haystack: List[int], needle: int) -> bool:
    for item in haystack:
        if item == needle:
            print(f"Needle: {needle} is in Haystack: {haystack}. True")
            return True

    print(f"Needle: {needle} is NOT in Haystack: {haystack}. False")
    return False
