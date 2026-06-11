"""
Given two lists, return True if they have at least 1 common member."""


def item_in_common_loop(list1, list2):
    """This is a brute-force solution with O(n*m) time complexity."""
    """O(n2)"""
    for i in list1:
        for j in list2:
            if i == j:
                return True
    return False


def item_in_common(list1, list2):
    """This is a hash table solution with O(n+m) time complexity."""
    """O(n)"""
    hash_table = {}
    for item in list1:
        hash_table[item] = True
    for item in list2:
        if item in hash_table:
            return True
    return False


list1 = [1, 2, 3, 4, 5]
list2 = [5, 6, 7, 8, 9]

print(item_in_common_loop(list1, list2))
print(item_in_common(list1, list2))
