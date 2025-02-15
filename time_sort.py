import time
import random

def tim_sort(lst):
    """Sorts a list using TimSort algorithm and returns the sorted list."""
    RUN = 32
    n = len(lst)
    for i in range(0, n, RUN):
        lst[i:i + RUN] = sorted(lst[i:i + RUN])
    size = RUN
    while size < n:
        for left in range(0, n, 2 * size):
            mid = left + size - 1
            right = min((left + 2 * size - 1), (n-1))
            lst[left:right+1] = sorted(lst[left:right+1])
        size *= 2
    return lst

# Generate a random list of numbers
items = [random.randint(1, 10000000) for _ in range(2000)]

# Measure time for TimSort
start_time = time.time()
sorted_items = tim_sort(items)
end_time = time.time()
processing_time_ms = (end_time - start_time) * 1000  # Convert seconds to milliseconds

print("\nTim Sort:")
print("Sorted items:", sorted_items)
print("Processing Time: {:.6f} seconds ({:.3f} ms)".format(end_time - start_time, processing_time_ms))

