import random
import time

def tim_sort(lst):
    """Sorts a list using a TimSort-like approach and returns the sorted list."""
    RUN = 32
    n = len(lst)
    # Sort small chunks using built-in sorted()
    for i in range(0, n, RUN):
        lst[i:i + RUN] = sorted(lst[i:i + RUN])
    size = RUN
    while size < n:
        for left in range(0, n, 2 * size):
            mid = left + size - 1
            right = min((left + 2 * size - 1), (n - 1))
            lst[left:right+1] = sorted(lst[left:right+1])
        size *= 2
    return lst

def generic_tim_sort(data):
    """
    Sorts various data structures:
      - For lists/tuples: returns the sorted list or tuple.
      - For sets: returns a sorted list (since sets are unordered).
      - For dictionaries: sorts by keys and returns a new dict.
    """
    if isinstance(data, dict):
        # Sort dictionary keys and reconstruct the dictionary
        sorted_keys = tim_sort(list(data.keys()))
        return {key: data[key] for key in sorted_keys}
    elif isinstance(data, tuple):
        sorted_list = tim_sort(list(data))
        return tuple(sorted_list)
    elif isinstance(data, set):
        return tim_sort(list(data))
    else:
        try:
            # Attempt to convert any iterable into a list for sorting
            return tim_sort(list(data))
        except TypeError:
            raise TypeError("Unsupported data structure for sorting.")

# Demonstration of the generic_tim_sort function
if __name__ == "__main__":
    # List example
    items_list = [random.randint(1, 100000) for _ in range(50)]
    print("Sorted List:", generic_tim_sort(items_list))

    # Tuple example
    items_tuple = tuple(random.randint(1, 100000) for _ in range(50))
    print("Sorted Tuple:", generic_tim_sort(items_tuple))

    # Set example
    items_set = {random.randint(1, 100000) for _ in range(50)}
    print("Sorted Set (as list):", generic_tim_sort(items_set))

    # Dictionary example
    items_dict = {i: random.randint(1, 100) for i in range(50)}
    print("Sorted Dictionary by keys:", generic_tim_sort(items_dict))

    # Measuring processing time for a list sort
    start_time = time.time()
    generic_tim_sort(items_list)
    end_time = time.time()
    processing_time_ms = (end_time - start_time) * 1000
    print("\nProcessing Time: {:.6f} seconds ({:.3f} ms)".format(end_time - start_time, processing_time_ms))
