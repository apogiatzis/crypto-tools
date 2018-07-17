import itertools

class PolybiusSquare():
    """
    Class to initialize square and invoke
    encrypt and decrypt operations."""

    def __init__(self, alphabet, key):
        l = len(alphabet)

        self.square = [[0 for x in range(l)] for y in range(l)] 
        # Create square from key
        assert len(key) == l**2
        for i in range(len(key)):
            self.square[int(i/4)][i%4] = key[i]
        # Create index map
        self.index_map = {}
        for i in range(l):
            self.index_map[alphabet[i]] = i
    
    def get_from_table(self, text):
        assert len(text)==2
        return self.square[self.index_map[text[0]]][self.index_map[text[1]]]

    def decrypt(self, message):
        plaintext = []
        for c in range(0, len(message),2):
            plaintext.append(self.get_from_table(message[c:c+2]))
        return ''.join(plaintext)

    def __str__(self):
        return str(self.square)


import itertools
possible_keys = itertools.permutations("0123456789abcdef", r=16)

i = 1
for p in possible_keys:
    print('[+] Trying key %d' % i)
    ps = PolybiusSquare("ATCG", ''.join(p))
    plaintext = ps.decrypt("CTGAAATGTTCCGCGAGCCGAACCGATTCACCGCCTAGAAACGTATTGTGCTGGTGTGCGGCGGTTAGAGATATTAGGTAGCGCCGTTACTCTAACATTTCGAATCAACCTTTCAGGGGAGTCACTGCCATCGTAAGTAGAGTACTTAGCATCGATGGCCATGCCTACTAATTACAGGCTGAATGACACTAAACCTTAGTTCACTGACCCGTTTTGTCATGTACTCTTGTGGTATGGGTCTTCAAATTGATCTGATTGGGAAGATAGAAAAACGGCTCTATCCTGGGTCGAGCCTCCCATGAAGCAGTCAAGGGGCCGCGAGGACTTCGATACTTGCCCTGCTCGAGCACATTTTAAAGCTTATTCCACATACTAGACTTACCCCCCGGCGTGTCGTACTGGAAGGTTAAACCTCTTGAGTTGATCTGACAACCTAGACGCGTGCCACGTTGTGTGGGATAGGTCACTCTCATTTCCACGAGGGACCAGAACCTTTGGCAATCCAGTTATTCTGCACTCGTGGCCGCCTCTCCTGGCAGGGGACCGGTAAGTTTGCGTATTCGCCGGGGAGTGGAGACGGATCGTCGTACACTGTTTCGAAAATTTTTGAGGATGGAGAGCAGAGCTATTGGATAAACGCTTGTACAGGTTCAATACTATTAGCAACGTGCCACCGGCACAGCTATCTCTGTTTCGCATGAAAGAGCCGTTAATCACGACGTTTAATCGAAACACATACCGATGGTCTACGAATATTATATCCGATACTAAGTCGGCCGCCGCAGTCCAGACGCCATATCGCTTTGAAGACCCCAAGGCGAACATTAACCGGTACGAGCAACTGCGGAGTGCCCTGCAATAGTCCGTCTGTAAAGGGCCCAGGCTAGGGCAAATAGTCCCTAAAACTAGAGATGGTCAACCGCTATGTGGGGCATTCTCCGTGAGACTCAGCCGTATTACAGTGAGCGTATTCCCAAACTCCCCTTCTGTGTATGACCAGTGTCGCTGCAAATGGACCGAGCAG")

    i +=1
    # Try decoding
    try:
        print(bytearray.fromhex(plaintext).decode())
        break
    except:
        continue
