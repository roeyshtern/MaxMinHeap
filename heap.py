import math

class MaxMinHeap:
    def __init__(self, data=None):
        if data is None:
            self.data = []
        else:
            self.data = data

    def parent(self, i):
        if(i-1 < 0):
            return -1
        return math.floor((i - 1) / 2)

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def size(self):
        return len(self.data)

    def swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]

    def print_heap(self):
        lines, *_ = self.display(0)
        for line in lines:
            print(line)

    def display(self, i):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.left(i) >= self.size() and self.right(i) >= self.size():
            line = '%s' % self.data[i]
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right(i) >= self.size():
            lines, n, p, x = self.display(self.left(i))
            s = '%s' % self.data[i]
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Two children.
        left, n, p, x = self.display(self.left(i))
        right, m, q, y = self.display(self.right(i))
        s = '%s' % self.data[i]
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    def height(self, index):
        if index == 0:
            return 0

        return math.floor(math.log2(index + 1))

    def build_heap(self): 
        for i in range(len(self.data) - 1, math.ceil((len(self.data) - 1) / 2), -1):
            self.heapify_node(i)

    def build_heap2(self): 
        for i in range(len(self.data) - 1, 0, -1):
            self.heapify_node(i)

    def heapify_node(self, index):
        current_parent_index = index
        while self.parent(current_parent_index) != -1:
            current_parent_index = self.parent(current_parent_index)
            if self.height(current_parent_index) % 2 == 0:
                if self.data[index] > self.data[current_parent_index]:
                    self.swap(index, current_parent_index)
                    self.heapify_node(index)
                    index = current_parent_index
            else:
                if self.data[index] < self.data[current_parent_index]:
                    self.swap(index, current_parent_index)
                    self.heapify_node(index)
                    index = current_parent_index