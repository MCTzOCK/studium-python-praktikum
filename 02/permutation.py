def isPermutation(list1, list2):
    if len(list1) != len(list2):
        return False

    remaining = list2.copy()
    for item in list1:
        try:
            remaining.remove(item)
        except ValueError:
            return False

    return True

# Testfälle
print(isPermutation([1, 2, 3], [3, 2, 1]))  # True
print(isPermutation(['a', 'b', 'c'], ['c', 'b', 'a']))  # True
print(isPermutation([1, 2, 3], [1, 2, 2]))  # False
print(isPermutation([1, 2, 3], [4, 5, 6]))  # False
print(isPermutation([], []))  # True
print(isPermutation([1, 2, 3], [1, 2]))  # False
print(isPermutation([1, "test", 3.14159, [], True, []], [1, "test", 3.14159, [], True, "test"])) # False