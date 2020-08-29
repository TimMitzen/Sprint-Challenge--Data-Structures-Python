class BSTNode:
    def __init__(self, value_node):
        self.value_node = value_node
        self.left_side: BSTNode = None
        self.right_side: BSTNode = None

    def insert_node(self,value):
        if value >= self.value_node:#inserting on the right side
            if self.right_side is None: #if there is no right side node
                new_node = BSTNode(value)
                self.right_side = new_node
            else:
                right_child = self.right_side
                right_child.insert_node(value)#reclusive
        if value < self.value_node:
            if self.left_side is None:
                self.left_side = BSTNode(value)
            else:
                left_child = self.left_side
                left_child.insert_node(value)

    def search_contains(self, target_node):
        if target_node is None:
            return None
        if target_node == self.value_node:
            return True
        if target_node > self.value_node:
            if self.right_side is None:
                return False
            else:
                return self.right_side.search_contains(target_node)#if the node is on the right
        if target_node < self.value_node:
            if self.left_side is None:
                return False
            else:
                return self.left_side.search_contains(target_node)#if the node is on the lesft

