import math
import random

from HeapUtils import *


class MaxMinHeap:
    def __init__(self, data=None):
        if data is None:
            self.data = []
        else:
            self.data = data

    def has_left(self, index):
        """This function checks if a given node in the heap has a left child"""
        return left(index) < self.size()

    def has_right(self, index):
        """This function checks if a given node in the heap has a right child"""
        return right(index) < self.size()

    def has_children(self, index):
        """This function checks if a given node in the heap has any children"""
        return self.has_left(index)

    def swap(self, i, j):
        """This function swaps the values"""
        self.data[i], self.data[j] = self.data[j], self.data[i]

    def print_heap(self):
        """This function prints the current state of the heap"""
        if self.size() == 0:
            print('Heap is empty. Use Build heap or Insert')
            return

        lines, *_ = self.display(0)
        for line in lines:
            print(line)

    def size(self):
        """This function returns the number of elements currently in the heap."""
        return len(self.data)

    def display(self, i):
        """This function recursively generates a visual representation of the binary heap."""
        # No child.
        if left(i) >= self.size() and right(i) >= self.size():
            line = '%s' % self.data[i]
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if right(i) >= self.size():
            lines, n, p, x = self.display(left(i))
            s = '%s' % self.data[i]
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Two children.
        left_index, n, p, x = self.display(left(i))
        right_index, m, q, y = self.display(right(i))
        s = '%s' % self.data[i]
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * \
            '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + \
            (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left_index += [n * ' '] * (q - p)
        elif q < p:
            right_index += [m * ' '] * (p - q)
        zipped_lines = zip(left_index, right_index)
        lines = [first_line, second_line] + \
            [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    def build_heap(self):
        """This function builds a max-min-heap."""
        last_not_leaf = math.floor((len(self.data) / 2) - 1)
        for i in range(last_not_leaf, -1, -1):
            self.heapify_node(i)

    def heapify_node(self, index):
        """This function selects the appropriate helper function to call based on whether the node is at a max or min level of the heap."""
        if not self.has_children(index):
            return

        if is_max_level(index):
            self.heapify_max(index)
        else:
            self.heapify_min(index)

    def heapify_max(self, index):
        """This function maintains the max heap."""
        max_children = self.find_max_children_and_grandchildren(index)
        if self.data[max_children] > self.data[index]:
            self.swap(max_children, index)
            if index == grandparent(max_children):
                if self.data[max_children] < self.data[parent(max_children)]:
                    self.swap(max_children, parent(max_children))

                self.heapify_node(max_children)

    def heapify_min(self, index):
        """This function maintains the min heap."""
        min_children = self.find_min_children_and_grandchildren(index)
        if self.data[min_children] < self.data[index]:
            self.swap(min_children, index)
            if index == grandparent(min_children):
                if self.data[min_children] > self.data[parent(min_children)]:
                    self.swap(min_children, parent(min_children))

                self.heapify_node(min_children)

    def get_children_and_grandchildren_list(self, index):
        """This function takes an index as input and returns a list of its immediate children and grandchildren indices in the heap"""
        children_and_granchildren = []
        if self.has_left(index):
            children_and_granchildren.append(left(index))
            if self.has_left(left(index)):
                children_and_granchildren.append(left(left(index)))

            if self.has_right(left(index)):
                children_and_granchildren.append(right(left(index)))

        if self.has_right(index):
            children_and_granchildren.append(right(index))
            if self.has_left(right(index)):
                children_and_granchildren.append(left(right(index)))

            if self.has_right(right(index)):
                children_and_granchildren.append(right(right(index)))

        return children_and_granchildren

    def find_max_children_and_grandchildren(self, index):
        """This function finds the index of the maximum value among the children and grandchildren of a node."""
        return self.find_max_in_index_list(self.get_children_and_grandchildren_list(index))

    def find_min_children_and_grandchildren(self, index):
        """This function finds the index of the minimum value among the children and grandchildren of a node."""
        return self.find_min_in_index_list(self.get_children_and_grandchildren_list(index))

    def find_max_in_index_list(self, index_list):
        """This function takes a list as input and iterates through the list to find the index with the maximum value in the heap data"""
        max_index = index_list[0]
        for i in index_list:
            if self.data[max_index] < self.data[i]:
                max_index = i

        return max_index

    def find_min_in_index_list(self, index_list):
        """This function takes a list as input and iterates through the list to find the index with the minimum value in the heap data"""
        min_index = index_list[0]
        for i in index_list:
            if self.data[min_index] > self.data[i]:
                min_index = i

        return min_index

    def push_up(self, index):
        """This function takes an index as input and performs heapify operation in upward direction from the given index."""
        current_parent_index = index
        while parent(current_parent_index) != -1:
            current_parent_index = parent(current_parent_index)
            if height(current_parent_index) % 2 == 0:
                if self.data[index] > self.data[current_parent_index]:
                    self.swap(index, current_parent_index)
                    index = current_parent_index
            else:
                if self.data[index] < self.data[current_parent_index]:
                    self.swap(index, current_parent_index)
                    index = current_parent_index

    def extract_max(self):
        """This function removes and returns the largest element from the heap"""
        if self.size() == 0:
            raise ValueError('Heap is empty. Use Build heap or Insert')

        max_element_index = 0
        last_index = self.size() - 1
        self.swap(max_element_index, last_index)
        max_element = self.data.pop()
        self.heapify_node(max_element_index)

        return max_element

    def extract_min(self):
        """This function removes and returns the smallest element from the heap"""
        if self.size() == 0:
            raise ValueError('Heap is empty. Use Build heap or Insert')
        if not self.has_right(0):
            return self.data.pop()

        min_element_index = 1
        if self.data[1] > self.data[2]:
            min_element_index = 2

        last_index = self.size() - 1
        self.swap(min_element_index, last_index)
        min_element = self.data.pop()
        self.heapify_node(min_element_index)

        return min_element

    def delete(self, index):
        """This function takes an index as input and deletes the node at that index from the heap data."""
        if index < 0 or index >= self.size():
            raise ValueError('Invalid index. Please enter a value between 0 and the heap\'s length.')

        last_index = self.size() - 1
        self.swap(index, last_index)
        self.data.pop()
        if index == last_index:
            return

        self.push_up(index)
        self.heapify_node(index)

    def insert(self, key):
        """ This functiont inserts a new element into the heap"""
        self.data.append(key)
        self.push_up(len(self.data) - 1)

    def print_sort(self):
        """This function sorts and prints the elements in the heap"""
        if self.size() == 0:
            raise ValueError('Heap is empty. Use Build heap or Insert')

        while self.size() > 0:
            print(self.extract_max(), end=' ')
        print()

    # For tests
    def do_random_op(self):
        chosen_op_index = random.randint(0, 3)
        rand_int = 0

        if chosen_op_index == 0:
            rand_int = random.randint(-100, 333)
            self.insert(rand_int)
        elif chosen_op_index == 1:
            if self.size() == 0:
                return

            rand_int = random.randint(0, self.size() - 1)
            self.delete(rand_int)
        elif chosen_op_index == 2:
            if self.size() == 0:
                return

            self.extract_min()
        elif chosen_op_index == 3:
            if self.size() == 0:
                return

            self.extract_max()
