import math

def parent(i):
    if(i-1 < 0):
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
