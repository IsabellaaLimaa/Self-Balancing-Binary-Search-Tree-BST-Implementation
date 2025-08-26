import unittest
from dictionary_bst import Node, DictionaryBST

class TestNode(unittest.TestCase):
    def test_init(self):
        '''test Node initalizes correctly'''
        root = Node("banana", "A yellow tropical fruit.")
        self.assertEqual(root.word, "banana")
        self.assertEqual(root.meaning, "A yellow tropical fruit.")
        self.assertFalse(root.left)
        self.assertFalse(root.right)
        self.assertEqual(root.weight, 1)
    def test_insert_left_and_right(self):
        '''Tests inserting nodes to the left and right of the root'''
        root = Node("banana", "A yellow tropical fruit.")
        root.insert("apple", "A fruit that grows on trees.")
        root.insert("cherry", "A small, round, red fruit.")

        self.assertEqual(root.left.word, "apple")
        self.assertEqual(root.left.meaning, "A fruit that grows on trees.")
        self.assertEqual(root.right.word, "cherry")
        self.assertEqual(root.right.meaning, "A small, round, red fruit.")
        root.insert("banana", "Updated")
        self.assertEqual(root.word, "banana")
        self.assertEqual(root.meaning, "Updated")

    
    def test_update_weight(self):
        '''Tests that update_weight returns the correct left/right sizes and updates weight'''
        root = Node("banana", "A yellow tropical fruit.")
        root.insert("apple", "A fruit that grows on trees.")
        root.insert("cherry", "A small, round, red fruit.")
        left_w, right_w = root.update_weight()
        self.assertEqual(left_w, 1)
        self.assertEqual(right_w, 1)
        self.assertEqual(root.weight, 3)

    def test_search(self):
        '''Tests searching for various nodes'''
        root = Node("banana", "A yellow tropical fruit.")
        root.insert("apple", "A fruit that grows on trees.")
        root.insert("cherry", "A small, round, red fruit.")
        self.assertEqual(root.search("banana"), "A yellow tropical fruit.")
        self.assertEqual(root.search("apple"), "A fruit that grows on trees.")
        self.assertEqual(root.search("cherry"), "A small, round, red fruit.")
        self.assertIsNone(root.search("peach"))

class TestDictionaryBST(unittest.TestCase):
    def test_init(self):
        '''Tests initializing DictionaryBST and inserting multiple entries'''
        dict = DictionaryBST()
        entries = {
            "banana": "A yellow tropical fruit.",
            "apple": "A fruit that grows on trees.",
            "cherry": "A small, round, red fruit."
        }
        for word, meaning in entries.items():
            dict.insert(word, meaning)

    def test_insert_root_then_left_and_right(self):
        '''Tests inserting into the BST when empty and then verifying structure'''
        dict = DictionaryBST()
        #if no root inserted value becomes the root
        self.assertIsNone(dict.root)
        dict.insert("banana", "A yellow tropical fruit.")
        self.assertIsNotNone(dict.root)
        self.assertEqual(dict.root.word, "banana")
        self.assertEqual(dict.root.meaning, "A yellow tropical fruit.")
        
        dict.insert("apple", "A fruit that grows on trees.")
        dict.insert("cherry", "A small, round, red fruit.")
        #words inserted are attached to the left is less than word or right if greater
        self.assertEqual(dict.root.left.word, "apple")
        self.assertEqual(dict.root.left.meaning, "A fruit that grows on trees.")
        self.assertEqual(dict.root.right.word, "cherry")
        self.assertEqual(dict.root.right.meaning, "A small, round, red fruit.")
        #inserting a word that is already there updates the meaning
        dict.insert("banana", "Updated")
        self.assertEqual(dict.root.word, "banana")
        self.assertEqual(dict.root.meaning, "Updated")


    def test_search(self):
        '''Tests searching for word'''
        dict = DictionaryBST()
        dict.insert("banana", "A yellow tropical fruit.")
        self.assertEqual(dict.search("banana"), "A yellow tropical fruit.")

    def test_search_empty(self):
        '''Tests search on an empty tree'''
        dict = DictionaryBST()
        self.assertIsNone(dict.search("grape"))

    def test_in_order_print(self):
        '''Tests the in-order traversal to return alphabetical list'''
        entries = {
            'apple': 'A fruit that grows on trees',
            'banana': 'A yellow fruit that monkeys like',
            'cat': 'A small domesticated carnivorous mammal',
            'dog': 'A domesticated carnivorous mammal'
        }
        dict = DictionaryBST(entries)
        expected = [
            ('apple', 'A fruit that grows on trees'),
            ('banana', 'A yellow fruit that monkeys like'),
            ('cat', 'A small domesticated carnivorous mammal'),
            ('dog', 'A domesticated carnivorous mammal')
        ]
        self.assertEqual(dict.print_alphabetical(), expected)
        print(expected)
        print(dict.print_alphabetical())

    def test_empty_dict(self):
        '''Tests print_alphabetical on an empty tree'''
        empty = DictionaryBST()
        self.assertEqual(empty.print_alphabetical(), [])
        
if __name__ == '__main__':
    '''runs the unittests'''
    unittest.main()
