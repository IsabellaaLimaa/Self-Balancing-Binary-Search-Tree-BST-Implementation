class Node:
    """
    A class to represent a node in the tree.
    """
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning
        self.left = None
        self.right = None
        self.weight = 1  # number of nodes in subtree rooted at this node

    def update_weight(self):
        '''update weight of the node based on length of each side'''
        left_w = self.left.weight if self.left else 0
        right_w = self.right.weight if self.right else 0
        self.weight = 1 + left_w + right_w
        return left_w, right_w

    def insert(self, word, meaning):
        """
        Insert a word and its meaning into the tree. If inserting a duplicate word updates the meaning.
        Args:
            word (str): The word to insert.
            meaning (str): The meaning of the word.
        """
        if word == self.word:
            self.meaning = meaning
        elif word < self.word:
            if self.left:
                self.left = self.left.insert(word, meaning)
            else:
                self.left = Node(word, meaning)
        else: # word > self.word
            if self.right:
                self.right = self.right.insert(word, meaning)
            else:
                self.right = Node(word, meaning)

        left_w, right_w = self.update_weight()

        # Self-balancing logic: rebalance if subtree is too unbalanced
        if (max(left_w, right_w) + 1) / (min(left_w, right_w) + 1) >= 3:
            if left_w > right_w:
                return self.rotate_right()
            elif left_w < right_w:
                return self.rotate_left()
        return self

    def rotate_left(self):
        '''rotate to the left if right side is heaver'''
        new_root = self.right
        self.right = new_root.left
        new_root.left = self

        self.update_weight()
        new_root.update_weight()

        return new_root

    def rotate_right(self):
        '''rotate to the right if left side is heaver'''
        new_root = self.left
        self.left = new_root.right
        new_root.right = self

        self.update_weight()
        new_root.update_weight()

        return new_root

    def search(self, word):
        """
        Search for a word in the tree and return its meaning.
        Args:
            word (str): The word to search for.
        Returns:
            str: The meaning of the word if found, else return None'
        """
        if word == self.word:
            return self.meaning
        elif word < self.word:
            return self.left.search(word) if self.left else None
        else:
            return self.right.search(word) if self.right else None


class DictionaryBST:
    """
        Parameters:
        entries (dict[str, str] | None, optional): A dictionary with string words and meanings.
                                                  Defaults to None if not provided.
    """
    def __init__(self, entries: dict[str, str] | None = None):
        """
        Initializes the dictionary tree with initial entries
        """
        self.root = None
        if entries:
            for word, meaning in entries.items():
                self.insert(word, meaning)

    def insert(self, word, meaning):
        """
        Insert a word and its meaning into the tree. If inserting a duplicate word updates the meaning.
        
        Args:
            word (str): The word to insert.
            meaning (str): The meaning of the word.
        """
        if self.root:
            self.root = self.root.insert(word, meaning)
        else:
            self.root = Node(word, meaning)

    def search(self, word):
        """
        Search for a word in the tree and return its meaning.
        
        Args:
            word (str): The word to search for.
        
        Returns:
            str: The meaning of the word if found, else return None'
        """
        if self.root:
            return self.root.search(word)  
        return None

    def in_order(self, node, entries):
        '''append nodes to entries in_order transversal'''
        if not node:
            return
        self.in_order(node.left, entries)
        entries.append((node.word, node.meaning))
        self.in_order(node.right, entries)

    def print_alphabetical(self):
        """
        Retrieve all dictionary entries in alphabetical order.
        
        Returns:
            list of tuple: List of tuples, each containing (word, meaning).
        """
        entries = []
        self.in_order(self.root, entries)
        return entries


if __name__ == '__main__':
    dictionary = DictionaryBST()
    dictionary.insert("banana", "A yellow tropical fruit.")
    dictionary.insert("apple", "A fruit that grows on trees.")
    dictionary.insert("cherry", "A small, round, red fruit.")
    print(dictionary.search("banana"))  # Output: A yellow tropical fruit.
    print(dictionary.print_alphabetical())
    # Expected:
    # [
    #     ("apple", "A fruit that grows on trees."),
    #     ("banana", "A yellow tropical fruit."),
    #     ("cherry", "A small, round, red fruit.")
    # ]
