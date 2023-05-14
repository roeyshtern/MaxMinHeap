import math
import os


def parent(i):
    if (i-1 < 0):
        return -1
    return math.floor((i - 1) / 2)


def grandparent(i):
    return parent(parent(i))


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def height(index):
    if index == 0:
        return 0

    return math.floor(math.log2(index + 1))


def is_max_level(index):
    return height(index) % 2 == 0


def check_if_heap_is_good(heap):
    for i in range(0, len(heap.data)):
        if is_max_level(i):
            if not check_children_lower(heap, i, heap.data[i]):
                return False
        else:
            if not check_children_greater(heap, i, heap.data[i]):
                return False
    return True


def check_children_lower(heap, curr_index, value):
    if heap.has_right(curr_index):
        return heap.data[curr_index] <= value and check_children_lower(heap, left(curr_index), value) and check_children_lower(heap, right(curr_index), value)
    elif heap.has_left(curr_index):
        return heap.data[curr_index] <= value and check_children_lower(heap, left(curr_index), value)
    else:
        return heap.data[curr_index] <= value


def check_children_greater(heap, curr_index, value):
    if heap.has_right(curr_index):
        return heap.data[curr_index] >= value and check_children_greater(heap, left(curr_index), value) and check_children_greater(heap, right(curr_index), value)
    elif heap.has_left(curr_index):
        return heap.data[curr_index] >= value and check_children_greater(heap, left(curr_index), value)
    else:
        return heap.data[curr_index] >= value

def fill_heap_data_from_file(heap, filename):
    if not os.path.exists(filename):
        raise ValueError('The file does not exist. Please check the file path and try again.')
    heap.data = get_values_from_file(filename)

def get_values_from_file(filename):
    with open(filename, 'r') as f:
        data = f.read().replace(',', '')
        values = [int(x) for x in data.split()]

    return values
