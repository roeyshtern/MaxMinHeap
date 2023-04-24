from heap import MaxMinHeap


def main():
  # Create a max min heap.
  heap = MaxMinHeap([
0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100
  ])

  # Check the size of the heap.
 # print("The size of the heap is", heap.size())
  # Print the heap.
  
  heap.build_heap()
  heap.print_heap()


  # Check the left, right and parent of the root node.
#  print("The left child of the root node is", heap.left(0))
#  print("The right child of the root node is", heap.right(0))
#  print("The parent of the root node is", heap.parent(0))

if __name__ == "__main__":
  main()
