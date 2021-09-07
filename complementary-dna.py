"""Complementary DNA"""

def DNA_strand(dna):
    # code here
    complement = {"A": "T", "T": "A", "C": "G", "G": "C"}
    
    dna = "".join(complement[letter] for letter in dna)
    
    return dna
