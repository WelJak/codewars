def sort_array(source_array):
    b = sorted([item for item in source_array if item%2 != 0])
    odd_int = 0
    for i in range(len(source_array)):
        if source_array[i] %2 != 0:
            source_array[i] = b[odd_int]
            odd_int += 1
    return source_array
