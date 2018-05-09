def binary_search(a, target, min_index = 0, max_index = -999, f = True):
    if f:
        max_index = len(a)
        f = False
    i = (max_index + min_index) // 2
    if a[i] == target:
        return i
    if max_index - min_index < 2:
        return -1
    if target < a[i]:
        max_index = i
        return binary_search(a, target, min_index, max_index, f)
    else:
        min_index = i
        return binary_search(a, target, min_index, max_index, f)
