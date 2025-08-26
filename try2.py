class Node:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning
        self.left = None
        self.right = None
        self.weight = 1  # Number of nodes in subtree rooted here

    def update_weight(self):
        left_weight = self.left.weight if self.left else 0
        right_weight = self.right.weight if self.right else 0
        self.weight = 1 + left_weight + right_weight
        return left_weight, right_weight

    def insert(self, word, meaning):
        if word == self.word:
            self.meaning = meaning
        elif word < self.word:
            if self.left:
                self.left = self.left.insert(word, meaning)
            else:
                self.left = Node(word, meaning)
        else:  # word > self.word
            if self.right:
                self.right = self.right.insert(word, meaning)
            else:
                self.right = Node(word, meaning)

        left_w, right_w = self.update_weight()

        # Self-balancing logic: rebalance if subtree is too unbalanced
        if (max(left_w, right_w) + 1) / (min(left_w, right_w) + 1) >= 3:
            if left_w > right_w:
                return self.rotate_right()
            else:
                return self.rotate_left()
        return self

    def rotate_left(self):
        new_root = self.right
        self.right = new_root.left
        new_root.left = self
        self.update_weight()
        new_root.update_weight()
        return new_root

    def rotate_right(self):
        new_root = self.left
        self.left = new_root.right
        new_root.right = self
        self.update_weight()
        new_root.update_weight()
        return new_root

    def search(self, word):
        if word == self.word:
            return self.meaning
        elif word < self.word:
            return self.left.search(word) if self.left else None
        else:
            return self.right.search(word) if self.right else None

    def in_order(self):
        if self.left:
            yield from self.left.in_order()
        yield (self.word, self.meaning)
        if self.right:
            yield from self.right.in_order()


class DictionaryBST:
    def __init__(self, entries=None):
        self.root = None
        if entries:
            for word, meaning in entries.items():
                self.insert(word, meaning)

    def insert(self, word, meaning):
        if not self.root:
            self.root = Node(word, meaning)
        else:
            self.root = self.root.insert(word, meaning)

    def search(self, word):
        if not self.root:
            raise KeyError(f"Word '{word}' not found.")
        result = self.root.search(word)
        if result is None:
            raise KeyError(f"Word '{word}' not found.")
        return result

    def print_alphabetical(self):
        if not self.root:
            return []
        return list(self.root.in_order())
    
if __name__ == '__main__':
    #Sample usage
    dictionary = DictionaryBST()
    dictionary.insert("banana", "A yellow tropical fruit.")
    dictionary.insert("apple", "A fruit that grows on trees.")
    dictionary.insert("cherry", "A small, round, red fruit.")
    # Search for a word
    print(dictionary.search("banana")) # Output: A yellow tropical fruit.
    # Print all entries in alphabetical order
    print(dictionary.print_alphabetical())
    # Output:
    # [
    # ("apple", "A fruit that grows on trees."),
    # ("banana", "A yellow tropical fruit."),
    # ("cherry", "A small, round, red fruit.")
    # ]