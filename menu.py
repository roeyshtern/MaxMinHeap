import os
import sys
from heap import MaxMinHeap
from HeapUtils import get_values_from_file, fill_heap_data_from_file

def build_heap(heap):
    filename = input('Enter filename: ')
    fill_heap_data_from_file(heap, filename)    
    heap.build_heap()


def sort_heap(heap):
    heap.print_sort()


def extract_max(heap):
    max_value = heap.extract_max()
    print(f'Max value extracted: {max_value}')


def extract_min(heap):
    min_value = heap.extract_min()
    print(f'Min value extracted: {min_value}')


def insert_value(heap):
    value = int(input('Enter value to insert: '))
    heap.insert(value)


def delete_index(heap):
    index = int(input('Enter index to delete: '))
    heap.delete(index)


def print_heap(heap):
    heap.print_heap()


def print_heap_menu():
    print('Heap menu:')
    print('1. Build heap')
    print('2. Sort heap')
    print('3. Extract max')
    print('4. Extract min')
    print('5. Insert value')
    print('6. Delete index')
    print('7. Print heap')
    print('8. Back to main menu')
    print('0. Exit')


def start():
    # Create a new Heap object
    heap = MaxMinHeap()
    print(sys.argv)
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        try:
            fill_heap_data_from_file(heap, filename)
        except ValueError as e:
            print(e)
            return
        heap.build_heap()
    # Do something with the second argument.
    while True:
        try:
            print_heap_menu()
            choice = int(input('Enter your choice: '))

            if choice == 0:
                print('Thank you for using our program.')
                return
            elif choice == 1:
                build_heap(heap)
            elif choice == 2:
                sort_heap(heap)
            elif choice == 3:
                extract_max(heap)
            elif choice == 4:
                extract_min(heap)
            elif choice == 5:
                insert_value(heap)
            elif choice == 6:
                delete_index(heap)
            elif choice == 7:
                print_heap(heap)
            elif choice == 8:
                break
            else:
                print('Invalid choice. Please try again.')

        except ValueError as e:
            print(e)
