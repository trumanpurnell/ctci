import math


class MinStack():
    def __init__(self):
        self.min = math.inf

        self.prev_mins = []
        self.stack = []

    def push(self, data):
        if data < self.min:
            self.min = data
            self.prev_mins.append(self.min)

        self.stack.append(data)

    def pop(self):
        popped = self.stack.pop()

        if popped == self.prev_mins[-1]:
            self.prev_mins.pop()
            self.min = self.prev_mins[-1]

        return popped


class MegaStack():
    def __init__(self, cap=10):
        self.stacks = []
        self.cap = cap

    def push(self, data):
        if not self.stacks or len(self.stacks[-1]) == self.cap:
            self.stacks.append([data])
            return

        self.stacks[-1].append(data)

    def pop(self, data):
        if not self.stacks:
            return

        if len(self.stacks[-1]) == 0:
            self.stacks.pop()  # removing empty last stack

        if self.stacks:
            return self.stacks[-1].pop()


class StackQueue():
    def __init__(self):
        self.back = []
        self.front = []

    def enqueue(self, data):
        self.back.append(data)

    def dequeue(self):
        if not self.front:

            if not self.back:
                return

            while self.back:
                self.front.append(self.back.pop())

        return self.front.pop()


def sort_stack(stack):
    sorted_stack = []

    while stack:
        num_to_insert = stack.pop()

        while sorted_stack and num_to_insert > sorted_stack[-1]:
            stack.append(sorted_stack.pop())

        sorted_stack.append(num_to_insert)

        while stack and sorted_stack[-1] >= stack[-1]:
            sorted_stack.append(stack.pop())
    
    return sorted_stack

class AnimalShelter():

    def __init__(self, dogs, cats):
        self.dogs = dogs
        self.cats = cats
    
    def dequeue_any(self):
        if not self.cats:
            return top_dog.pop(0) 
        
        if not self.dogs:
            return top_cat.pop(0)


        top_dog = self.dogs[0]
        top_cat = self.cats[0]
       
        if top_dog.time < top_cat.time:
            return top_dog.pop(0)
        else:
            return top_cat.pop(0)
    
    def dequeue(self, animal_list='dogs'):
        if getattr(self, animal_list):
            return getattr(self, animal_list).pop(0)
    