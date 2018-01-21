from collections import Counter
from math import isclose
from typing import Dict, List


class Node:
    def __init__(self, weight: float):
        self.weight = weight


class Leaf(Node):
    def __init__(self, value: chr, weight: float):
        self.value = value
        super().__init__(weight)

    def __str__(self):
        return f"{self.value}: {self.weight}"

    def __eq__(self, other):
        return self.value == other.value and isclose(self.weight, other.weight)

    def __ne__(self, other):
        return self.value != other.value or not isclose(self.weight, other.weight)


class InternalNode(Node):
    def __init__(self, weight: float, left: Node=None, right: Node=None):
        self.left = left
        self.right = right
        super().__init__(weight)


CODETYPE = {chr, str}


class HuffmanTree:
    """Implements a huffman codec. Source: https://en.wikipedia.org/wiki/Huffman_coding"""

    def __init__(self):
        self.tree: InternalNode = None
        self.code: CODETYPE = None
        self.leafs: [Leaf] = None

    def compress(self, text: str) -> str:
        """
            Compresses a text using the optimal Huffman code and returns
            the encoded string.
            The properties code, tree and leafs are set after running this method.
            :param text:str: The text to compress
        """
        self.leafs = HuffmanTree.sort_leafs(HuffmanTree.create_leafs(text))
        nodes: [Node] = list(self.leafs)
        if not nodes:
            return ""
        if len(nodes) == 1:
            nodes = [InternalNode(1, nodes[0])]
        return self.__compress(text, nodes)

    @staticmethod
    def sort_leafs(input_leafs: [Leaf]) -> [Leaf]:
        """
            Returns input_leafs sorted by weight (lowest first).
            :param input_leafs:[Leaf]: Leafs to sort.
        """
        return sorted(input_leafs, key=lambda x: x.weight)

    @staticmethod
    def create_leafs(text: str) -> [Leaf]:
        """
            Returns leafs for a given text.
            :param text:str: Text to generate leafs from.
        """
        return map(lambda t: Leaf(
            t[0], t[1] / len(text)), Counter(text).items())

    def __compress(self, text: str, nodes: [Node]) -> str:
        while len(nodes) > 1:
            leaf0 = nodes[0]
            leaf1 = nodes[1]
            internal_node = InternalNode(
                leaf0.weight + leaf1.weight, leaf0, leaf1)
            nodes = nodes[2:]
            nodes.append(internal_node)
        self.tree = nodes[0]
        self.code = HuffmanTree.compute_code(self.tree)
        return HuffmanTree.encode(text, self.code)

    @staticmethod
    def compute_code(tree: InternalNode, largest_word="") -> CODETYPE:
        """
            Iteratively computes the code from a Huffman tree.
            :param tree:InternalNode: Current root node of the Huffman tree
            :param largest_word="": Code for the root node.
        """
        code = dict()
        for node, bit in [(tree.left, "0"), (tree.right, "1")]:
            if isinstance(node, Leaf):
                code[node.value] = largest_word + bit
            elif node is not None:
                code.update(HuffmanTree.compute_code(node, largest_word + bit))

        return code

    @staticmethod
    def encode(text: str, code: CODETYPE) -> str:
        """
            Encodes a given string using a given Huffman code.
            :param text:str: The text to encode.
            :param code:dict: The code to use.
        """
        result = ""
        for letter in text:
            if letter not in code:
                raise Exception(f"Could not find code for {letter}!")
            result += code[letter]
        return result

    @staticmethod
    def decode(text: str, code: CODETYPE) -> str:
        """
            Decodes a string using a given Huffman code.
            :param text:str: The encoded string.
            :param code:dict: The Huffman code: {"<chr>": "<code>"}
        """
        reversed_code = {y: x for x, y in code.items()}
        result = ""
        acc = ""
        while text != "":
            acc += text[0]
            text = text[1:]
            if acc in reversed_code:
                result += reversed_code[acc]
                acc = ""
        if acc != "":
            raise Exception(
                f"Could not decode text, final accumulator: {acc}!")

        return result
