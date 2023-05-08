from heap import MaxMinHeap
from HeapUtils import check_if_heap_is_good
from menu import start
import random

def main():
    start()

def test_randoms():
    for _ in range(10000):
        heap = MaxMinHeap(generate_random_list())
        heap.build_heap()
        num_of_ops = random.randint(1, 3000)
        for _ in range(num_of_ops):
            heap.do_random_op()
            assert check_if_heap_is_good(heap) 

def generate_random_list():
    list_size = random.randint(0, 40)
    ret_list = []
    for _ in range(list_size):
        ret_list.append(random.randint(-20, 100))

    return ret_list


if __name__ == '__main__':
    main()
