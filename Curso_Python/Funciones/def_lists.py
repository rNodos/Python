array = [2, 6, 78, 4]

def list_sum(lst):
    s = 0

    for elem in lst:
        s += elem

    return s

print(list_sum(array))