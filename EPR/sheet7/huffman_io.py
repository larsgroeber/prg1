"""Example."""

import os
import csv
import json
import math
import tkinter as tk
import tkinter.filedialog as tkfiledialog
#from mimetypes import guess_type
#from collections import OrderedDict
import huffman

class HuffmanIO(huffman.HuffmanTree):
    """
       Series of methods to decompress and save Huffman encoded
       binary files or to compress text files via Huffman encoding.
    """
    def __init__(self):
        super().__init__()
        self.header = [
            "Symbol",
            "Absolute Occurences",
            "Relative Occurences",
            "Information Density",
            "Huffman Code Sequence",
        ]

    def process_huffman(self, path: str) -> None:
        """
           Process a text file. Generate Leafs, Tree, Code for Huffman
           compression and decompression.
        """
        filename, _file_extension = os.path.splitext(path)
        output_path = filename + ".bin"
        code_book_path = filename + ".json"
        statistic_path = filename + ".csv"

        with open(path, 'r+') as file,\
             open(output_path, 'wb') as output,\
             open(code_book_path, 'w') as code_book_file,\
             open(statistic_path, 'w', newline='') as csvfile:

            text = file.read()
            encoded_text = self.compress(text)
            code = self.code
            code_book_file.write(json.dumps(code))

            padded_encoded_text = self.prep_encoded_text(encoded_text)
            byte_array = self.build_byte_array(padded_encoded_text)
            output.write(bytes(byte_array))

            sorted_leafs = self.leafs
            stats = csv.writer(csvfile, delimiter=',', quotechar='"')

            stats.writerow(self.header)
            for leaf in reversed(sorted_leafs):
                symbol = leaf.value
                if symbol == "\n":
                    symbol = "\\n"
                elif symbol == " ":
                    symbol = "space"
                stats.writerow([symbol,
                                leaf.weight*len(text),
                                leaf.weight,
                                -math.log2(leaf.weight),
                                '= "' + str(code[leaf.value]) + '"',
                               ])

        bytes_bef = os.path.getsize(path)
        bytes_aft = os.path.getsize(output_path)
        bytes_code = os.path.getsize(code_book_path)
        print("Bytes before:", bytes_bef, "bytes")
        print("Bytes after:", bytes_aft, "bytes")
        print("Bytes codefile:", bytes_code, "bytes")
        print("Compression ratio bin/txt:", bytes_aft/bytes_bef*100, "%")
        print("Compression ratio (bin+json)/txt:",
              (bytes_aft+bytes_code)/bytes_bef*100, "%")
        print("Compressed!")


    @staticmethod
    def prep_encoded_text(encoded_text: str) -> str:
        """
           Add zeros to incomplete byte at the end of the
           bitstring generated through huffman encoding.
           and save the information at the start as 8 bit 
           integer word.
        """
        extra_padding = 8 - len(encoded_text) % 8
        for i in range(extra_padding):
            encoded_text += "0"
        padded_info = "{0:08b}".format(extra_padding)
        encoded_text = padded_info + encoded_text
        return encoded_text

    @staticmethod
    def build_byte_array(padded_encoded_text: str) -> bytearray:
        """
           From a bitstring, construct bytes, write them to
           a bytearray.
        """
        if len(padded_encoded_text) % 8 != 0:
            print("Encoded text not padded properly!")
            exit(0)
        byte_array = bytearray()
        for i in range(0, len(padded_encoded_text), 8):
            byte = padded_encoded_text[i:i+8]
            byte_array.append(int(byte, 2))
        return byte_array

    @staticmethod
    def reconstruct_coded_string(path: str) -> None:
        """
           Reconstruct a text from huffman encoded binary file
           and output it to a file.
        """
        filename, _file_extension = os.path.splitext(path)
        
        bitstring = ""
        for bit in HuffmanIO.bitstring_generator(path):
            bitstring += bit
        padding = int(bitstring[:8], 2)
        encoded_text = bitstring[8:-padding]

        codefile = filename + ".json"
        with open(codefile, 'r') as codec:
            code = dict(json.load(codec))

        newfile = filename + "_decompressed" + ".txt"
        with open(newfile, 'w') as output:
            output.write(huffman.HuffmanTree.decode(encoded_text, code))
        print("Decompressed!")

    @staticmethod
    def bitstring_generator(path: str) -> int:
        with open(path, 'rb') as bin_file:
            all_bytes = (byte for byte in bin_file.read())
            for byte in all_bytes:
                for i in reversed(range(8)):
                    yield str((byte >> i) & 1)

    @staticmethod
    def write_statistics(parameter_list):
        pass


class HuffmanUI(HuffmanIO):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.frame_top = tk.Frame(self.parent)
        self.menubar = tk.Menu(self.frame_top)
        self.parent.config(menu=self.menubar)

        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Open", command=self.onOpenFileDialog)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.parent.quit)
        self.menubar.add_cascade(label="File", menu=self.filemenu)

        self.frame_top.grid(row=0, columnspan=1, sticky="nsew")

    def onOpenFileDialog(self):
        """
           Grabs file and processes text/data in it.
        """
        ftypes = [('Text files', '*.txt'), ('Binary Files', '*.bin')]
        filedialogue = tkfiledialog.Open(self.parent, filetypes=ftypes)
        file = filedialogue.show()

        if file != '':
            _filename, file_extension = os.path.splitext(file)
            print("#"*79)
            print(file)
            if file_extension == ".txt":
                self.process_huffman(file)
            elif file_extension == ".bin":
                self.reconstruct_coded_string(file)


def main():
    """Main method, create app and execute."""
    root = tk.Tk()
    app = HuffmanUI(root)
    root.geometry("240x120")
    root.mainloop()


if __name__ == '__main__':
    main()
