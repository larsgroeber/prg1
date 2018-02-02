import unittest

from huffman import HuffmanTree, Leaf, InternalNode


class HuffmanTreeTest(unittest.TestCase):
    def setUp(self):
        self.huffman = HuffmanTree()
        self.addTypeEqualityFunc(Leaf, self.do_leafs_equal)

    def test_construct(self):
        self.assertIsNotNone(self.huffman)

    def test_leaf_sorting(self):
        leafs = [
            Leaf(1, 0.4),
            Leaf(1, 0.1),
            Leaf(1, 0.2),
            Leaf(1, 0.1),
            Leaf(1, 0.3),
        ]
        sorted_leafs = [
            Leaf(1, 0.1),
            Leaf(1, 0.1),
            Leaf(1, 0.2),
            Leaf(1, 0.3),
            Leaf(1, 0.4),
        ]
        self.do_lists_of_leafs_equal(
            sorted_leafs, HuffmanTree.sort_leafs(leafs))

    def test_create_leafs(self):
        leafs = HuffmanTree.create_leafs("test")
        expect = [Leaf("t", 0.5), Leaf("e", 0.25), Leaf("s", 0.25)]
        self.do_lists_of_leafs_equal(list(leafs), expect)

        leafs = HuffmanTree.create_leafs("aaaaaaaAAAAbbbbb eee")
        expect = [Leaf("a", 0.35), Leaf("A", 0.2), Leaf(
            "b", 0.25), Leaf(" ", 0.05), Leaf("e", 0.15)]
        self.do_lists_of_leafs_equal(list(leafs), expect)

    def test_compute_code(self):
        tree = InternalNode(1, Leaf("a", 0.5), Leaf("b", 0.5))
        code = HuffmanTree.compute_code(tree)
        self.assertEqual(code, {'a': '0', 'b': '1'})
        tree = InternalNode(1, Leaf("a", 0.5),
                            InternalNode(0.5, Leaf("b", 0.25), Leaf("c", 0.25)))
        code = HuffmanTree.compute_code(tree)
        self.assertEqual(code, {'a': '0', 'b': '10', 'c': '11'})
        tree = InternalNode(1, Leaf("a", 0.5),
                            InternalNode(0.5, Leaf("b", 0.25),
                                         InternalNode(0.25, Leaf("c", 0.1), Leaf("d", 0.15))))
        code = HuffmanTree.compute_code(tree)
        self.assertEqual(code, {'a': '0', 'b': '10', 'c': '110', 'd': '111'})

    def test_encode(self):
        code = {'a': '0', 'b': '1'}
        self.assertEqual(HuffmanTree.encode("ababbab", code), "0101101")
        self.assertEqual(HuffmanTree.encode("", code), "")
        code = {'a': '0', 'b': '1'}
        self.assertRaises(Exception, HuffmanTree.encode, "abcabbab", code)

    def test_compress(self):
        self.assertEqual(self.huffman.compress("test"), "010110")
        self.assertEqual(self.huffman.compress("AAAABBCC"), "000010101111")
        self.assertEqual(self.huffman.compress("AAAA"), "0000")
        self.assertEqual(self.huffman.compress("AAAA\nAAA"), "11110111")

    def test_decode(self):
        self.assertEqual(HuffmanTree.decode(
            "010110", {"t": "0", "e": "10", "s": "11"}), "test")
        self.assertEqual(HuffmanTree.decode(
            "00101111100", {"t": "00", "e": "1011", "s": "111"}), "test")
        self.assertRaises(Exception, HuffmanTree.decode,
                          "0101101", {"t": "0", "e": "10", "s": "11"})

    def do_leafs_equal(self, a: Leaf, b: Leaf, msg=None):
        if a != b:
            raise self.failureException(f"{a} does not match {b}!")

    def do_lists_of_leafs_equal(self, a: [Leaf], b: [Leaf], msg=None):
        for i, leaf in enumerate(a):
            if i >= len(b):
                self.failureException("Lists of leafs do not match!")
            self.assertEqual(leaf, b[i])


if __name__ == "__main__":
    unittest.main()
