from heap import MaxMinHeap


def main():
  # Create a max min heap
  list_with_one_bad_8 = [
    10, 0, 2, 8, 9, 5, 6, 7, 33, 1, 4
  ]

  list_with_one_bad_5 = [
    10, 0, 2, 8, 9, 15, 6, 7, 3, 1, 4
  ]

  list_with_one_bad_3 = [
    10, 0, 2, 18, 9, 5, 6, 7, 3, 1, 4
  ]

  list_with_one_bad_0 = [
    4, 0, 2, 8, 9, 5, 6, 4, 3, 1
  ]

  random_list = [
49, 55, 37, 31, 5, 13, 25, 19, 59, 7, 9, 11, 17, 29, 23, 53, 47, 51, 43, 15, 45, 39, 57, 41, 21, 27, 33, 35
  ]

  heap = MaxMinHeap(random_list)
  heap.build_heap()
  heap.print_heap()
  print(heap.extract_max())
  heap.print_heap()
  print(heap.extract_max())
  heap.print_heap()
  print(heap.extract_max())
  heap.print_heap()
  print(heap.extract_max())
  heap.print_heap()


if __name__ == "__main__":
  main()
