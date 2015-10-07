import time

def timed_sort(list, key):
    start_time   = time.time()
    sorted_list  = sorted(list, key=key)
    end_time     = time.time()
    elapsed_time = end_time - start_time
    return (sorted_list, elapsed_time)
