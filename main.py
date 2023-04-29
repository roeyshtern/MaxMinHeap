from heap import MaxMinHeap


def main():
  # Create a max min heap.
  heap = MaxMinHeap([
0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
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
