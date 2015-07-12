"""
A collection of solutions to common interview problems.
"""

def permute_string(string):
    """ Returns a list of all possible permutations of string
    """
    if len(string) == 1:
        return [string]

    permuted = []
    used_chars = []
    for idx, char in enumerate(string):
        # skip if dupe
        if char in used_chars:
            continue
        used_chars.append(char)

        substring = string[0:idx]+string[idx+1:]
        for permuted_substring in permute_string(substring):
            permuted.append(char+permuted_substring)

    return permuted


def rand7():
    """ Given rand5 implement rand7
    """
    from random import randint

    count = 0
    rand7_dict = {}
    for i in range(6):
        for j in range(6):
            rand7_dict[(i, j)] = count
            count += 1

    rand5_tup = (randint(0,5), randint(0,5))
    while rand7_dict[rand5_tup] >= 32:
        rand5_tup = (randint(0,5), randint(0,5))

    return rand7_dict[rand5_tup] % 8


class bst(object):
    """ Implementation of bst
    """
    @staticmethod
    def min_node(node):
        while node.left is not None:
            node = node.left
        return node
    

    @staticmethod
    def search(node, number):
        if number == node.value:
            return node
        elif number < node.value and node.left is not None:
            return bst.search(node.left, number)
        elif number > node.value and node.right is not None:
            return bst.search(node.right, number)            
        else:
            return


    def __init__(self, num):
        self.left = None
        self.right = None
        self.parent = None
        
        self.value = num

        
    def add(self, number):
        if self.value is None:
            self.value = number
        elif number <= self.value:
            if self.left is None:
                self.left = bst(number)
                self.left.parent = self
            else:
                self.left.add(number)
        else:
            if self.right is None:
                self.right = bst(number)
                self.left.parent = self
            else:
                self.right.add(number)

                
    def remove(self, node):
        if node.parent:
            if node.parent.value > node.value:
                node.parent.left = None
            else:
                node.parent.right = None
        else:
            node.value = None


    def update_parent(self, parent, node):
        if parent.value < node.value:
            parent.right = node
        else:
            parent.left = node

            
    def delete(self, number):
        node = bst.search(self, number)
        if node is not None:
            if node.left is None and node.right is None:
                self.remove(node)
            elif node.left is not None and node.right is not None:
                min_node = bst.min_node(node.right)
                node.value = min_node.value
                self.remove(min_node)
            elif node.left is None:
                self.update_parent(node.parent, node.right)
            elif node.right is None:
                self.update_parent(node.parent, node.left)
