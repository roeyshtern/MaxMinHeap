
import os
from heap import MaxMinHeap

def build_heap(heap):
    filename = input("Enter filename: ")
    if not os.path.exists(filename):
        print('The file does not exist.\n')
        raise ValueError()
    heap.build_heap(filename)

def heapify(heap):
    index = int(input("Enter index to heapify: "))
    if index < 0 or index >= heap.size():
        print("Invalid index. Please try again.\n")
        raise ValueError()
    else:
        heap.heapify_node(index)

def extract_max(heap):
    if heap.size() == 0:
        print("Heap is empty.")
    else:
        max_value = heap.extract_max()
        print(f"Max value extracted: {max_value}")

def extract_min(heap):
    if heap.size() == 0:
        print("Heap is empty.")
    else:
        min_value = heap.extract_min()
        print(f"Min value extracted: {min_value}")

def insert_value(heap):
    value = int(input("Enter value to insert: "))
    heap.insert(value)

def delete_index(heap):
    index = int(input("Enter index to delete: "))
    if index < 0 or index >= heap.size():
        print("Invalid index. Please try again.")
    else:
        heap.delete(index)

def print_heap(heap):
    heap.print_heap()

def print_main_menu():
    print("Main menu:")
    print("1. Build heap")
    print("0. Exit")

def print_heap_menu():
    print("Heap menu:")
    print("1. Heapify")
    print("2. Extract max")
    print("3. Extract min")
    print("4. Insert value")
    print("5. Delete index")
    print("6. Print heap")
    print("7. Back to main menu")
    print("0. Exit")

def start():
    # Create a new Heap object
    heap = MaxMinHeap()

    while True:
        print_main_menu()
        choice = int(input("Enter your choice: "))
        if choice == 0:
            print("Thank you for using our program.")
            break
        elif choice == 1:
            try:
                build_heap(heap)
            except ValueError:
                continue
            while True:
                print_heap_menu()
                choice = int(input("Enter your choice: "))
                if choice == 0:
                    return
                elif choice == 1:
                    try:
                        heapify(heap)
                    except ValueError:
                        continue
                elif choice == 2:
                    extract_max(heap)
                elif choice == 3:
                    extract_min(heap)
                elif choice == 4:
                    insert_value(heap)
                elif choice == 5:
                    try:
                        delete_index(heap)
                    except ValueError:
                        continue
                elif choice == 6:
                    print_heap(heap)
                elif choice == 7:
                    break
                else:
                    print("Invalid choice. Please try again.")
        else:
            print("Invalid choice. Please try again.")
