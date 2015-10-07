import time

def timed_sort(list, key, algorithm='insertion'):
    sort_func = globals()[algorithm]
    start_time   = time.time()
    sorted_list  = sort_func(list, key=key)
    end_time     = time.time()
    elapsed_time = end_time - start_time
    return (sorted_list, elapsed_time)

# ---
# Define your search algorithm functions here!

def insertion(list, key):
    size = len(list)
    for i in range(1, size):
        for j in range(i, 0, -1):
            compare = list[j - 1]
            current = list[j]
            if key(current) < key(compare):
                list[j] = compare
                list[j - 1] = current

    return list
