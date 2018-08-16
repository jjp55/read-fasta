making a trival change because he is not explaining anythingo

import sys

def read_fasta(filename):
    sequence = ''
	"""Reads a FASTA sequence from a file and returns it"""
    f = open(filename)
    for line in f:
        line = line.strip()
        if '>' not in line:
            sequence=sequence+line
    f.close()
    return sequence

if len(sys.argv) < 2
	print('Usage:', sys.argv[0], '<sequence.fa>')
	exit(1)
	
print(read_fasta('sys.argv[1]'))

