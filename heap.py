import math
from HeapUtils import *

class MaxMinHeap:
    def __init__(self, data=None):
        if data is None:
            self.data = []
        else:
            self.data = data

    def has_left(self, index):
        return left(index) < self.size()

    def has_right(self, index):
        return right(index) < self.size()

    def has_children(self, index):
        return self.has_left(index)

    def swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]

    def print_heap(self):
        lines, *_ = self.display(0)
        for line in lines:
            print(line)

    def size(self):
        return len(self.data)

    def display(self, i):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if  left(i) >= self.size() and right(i) >= self.size():
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
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left_index += [n * ' '] * (q - p)
        elif q < p:
            right_index += [m * ' '] * (p - q)
        zipped_lines = zip(left_index, right_index)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    def build_heap(self): 
        last_not_leaf = math.floor((len(self.data) / 2) - 1)
        for i in range(last_not_leaf, -1, -1):
            self.heapify_node(i)

    def heapify_node(self, index):
        if not self.has_children(index):
            return

        if is_max_level(index):
            self.heapify_max(index)
        else:
            self.heapify_min(index)
            
    def heapify_max(self, index):
        max_children = self.find_max_children_and_grandchildren(index)
        if self.data[max_children] > self.data[index]:
            self.swap(max_children, index)
            if index == grandparent(max_children):
                if self.data[max_children] < self.data[parent(max_children)]:
                    self.swap(max_children, parent(max_children))
                
                self.heapify_node(max_children)

    def heapify_min(self, index):
        min_children = self.find_min_children_and_grandchildren(index)
        if self.data[min_children] < self.data[index]:
            self.swap(min_children, index)
            if index == grandparent(min_children):
                if self.data[min_children] > self.data[parent(min_children)]:
                    self.swap(min_children, parent(min_children))
                
                self.heapify_node(min_children)

    def get_children_and_grandchildren_list(self, index):
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
        return self.find_max_in_index_list(self.get_children_and_grandchildren_list(index))

    def find_min_children_and_grandchildren(self, index):
        return self.find_min_in_index_list(self.get_children_and_grandchildren_list(index))

    def find_max_in_index_list(self, index_list):
        max_index = index_list[0]
        for i in index_list:
            if self.data[max_index] < self.data[i]:
                max_index = i
        
        return max_index
        
    def find_min_in_index_list(self, index_list):
        min_index = index_list[0]
        for i in index_list:
            if self.data[min_index] > self.data[i]:
                min_index = i
        
        return min_index
