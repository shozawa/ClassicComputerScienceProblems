class CompressedGene:
    def __init__(self, gene: str) -> None:
        self.__compress(gene)

    def __compress(self, gene: str) -> None:
        self.bit_string = 1
        for nucleotide in gene.upper():
            self.bit_string <<= 2
            if nucleotide == "A":
                self.bit_string |= 0b00
            elif nucleotide == "C":
                self.bit_string |= 0b01
            elif nucleotide == "G":
                self.bit_string |= 0b10
            elif nucleotide == "T":
                self.bit_string |= 0b11
            else:
                raise ValueError("Invalid Nucleotide:{}".format(nucleotide))
        pass

    def decompress(self) -> str:
        gene = ""
        for i in range(0, self.bit_string.bit_length() - 1, 2):
            bits = self.bit_string >> i & 0b11
            if bits == 0b00:
                gene += "A"
            elif bits == 0b01:
                gene += "C"
            elif bits == 0b10:
                gene += "G"
            elif bits == 0b11:
                gene += "T"
            else:
                raise ValueError("Invalid bits:{}".format(bits))
        return gene[::-1]

    def __str__(self) -> str:
        return self.decompress()


if __name__ == "__main__":
    from sys import getsizeof

    original = "TAGGGATTAACCG" * 1000
    compressed = CompressedGene(original)
    print("original is {} bytes.".format(getsizeof(original)))
    print("compressed is {} bytes.".format(getsizeof(compressed.bit_string)))
    print("original and compressed ares same: {}.".format(original == compressed.decompress()))
