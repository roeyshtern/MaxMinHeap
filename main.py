import random

from heap import MaxMinHeap
from HeapUtils import *
from menu import start


def main():
    #test_randoms()
    star    t()


def test_randoms():
    for i in range(1000):
        heap = MaxMinHeap(get_values_from_file(f'tests/test_{i}'))
        heap.build_heap()
        num_of_ops = random.randint(1, 3000)
        for _ in range(num_of_ops):
            heap.do_random_op()
            assert check_if_heap_is_good(heap)


if __name__ == '__main__':
    main()
