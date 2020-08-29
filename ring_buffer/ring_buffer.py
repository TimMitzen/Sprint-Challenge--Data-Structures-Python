class RingBuffer:
    def __init__(self, capacity):
        self.ring_buffer_data = []
        self.capacity = capacity
        self.index = 0



    def append(self, item):
        if self.ring_buffer_data < self.capacity:#if the rbd is less than cap append
            self.ring_buffer_data.append(item)
        else:
            self.ring_buffer_data[self.index] = item
            self.index += 1
            if self.index == self.capacity:
                self.index = 0

    def get(self):
        return self.ring_buffer_data