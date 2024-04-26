
#!/usr/bin/python3
"""
   this function finds a peak in a list of unsorted integers
"""

def find_peak(list):
    '''
        Finds the peak in a list of numbers
    '''
    length = len(list)
    if length == 0:
        return Null
    if length == 1:
        return (list[0])
    if length == 2:
        return list[0] if list[0] >= list[1] else list[1]

    for x in range(0, length):
        value = list[x]
        if (x > 0 and x < length - 1 and
                list[x + 1] <= value and list[x - 1] <= value):
                return value
        elif x == 0 and list[x + 1] <= value:
            return value
        elif x == length - 1 and list[x - 1] <= value:
            return value
    return value
