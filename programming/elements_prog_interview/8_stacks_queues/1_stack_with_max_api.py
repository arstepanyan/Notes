# Design a stack that includes a max operation, in addition to push and pop
class Stack:
    def __init__(self):
        self.items = []
        self.cached_maxes = []

    def isEmpty(self):
        return self.items == []

    def max(self):
        if self.isEmpty():
            raise IndexError('max(): stack is empty')
        return self.cached_maxes[-1][0]

    def pop(self):
        if self.isEmpty():
            raise IndexError('pop(): stack is empty')
        else:
            pop_el = self.items.pop()
            current_max = self.cached_maxes[-1][0]
            if pop_el == current_max:
                if self.cached_maxes[-1][1]-1 == 0:
                    self.cached_maxes.pop()
            return pop_el

    def push(self, item):
        self.items.append(item)
        if len(self.cached_maxes) == 0:
            self.cached_maxes.append([item, 1])
        else:
            cur_max = self.cached_maxes[-1][0]
            if item == cur_max:
                self.cached_maxes[-1][1] += 1
            elif item > cur_max:
                self.cached_maxes.append([item, 1])

if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(19)
    s.push(50)
    s.push(3)
    print(f's.items .... {s.items}')
    print(f's.max() .... {s.max()}')
    s.pop()
    s.pop()
    print(f's.items after 2 pops .... {s.items}')
    print(f's.max() ................. {s.max()}')
    s.pop()
    s.pop()
    print(f's.items after 2 more pops ......... {s.items}')
    print(f's.max() ........................... {s.max()}')