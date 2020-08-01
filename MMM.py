

def mean(list):
    if len(list) == 0:
        return 0
    total = 0
    for value in list:
        total += value
    return total / len(list)


def mode(list):
    if len(list) == 0:
        return 0
    set(list)
    maximum = max(set(list), key=list.count)
    return maximum


def median(list):
    if len(list) == 0:
        return 0
    list.sort()
    midterm = int(len(list)) // 2
    if len(list) % 2 == 1:
        return (list[midterm])
    else:
        return ((list[midterm] + list[midterm - 1]) / 2)


def main():

    list = [11, 12, 13, 14, 15, 16]

    print("List: ", list)
    print("Mode: ", mode(list))
    print("Median: ", median(list))
    print("Mean: ", mean(list))


main()
