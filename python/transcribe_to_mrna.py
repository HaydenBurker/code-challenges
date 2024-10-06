# Create a function that converts a DNA strand to its corresponding mRNA strand

def dna_to_mrna(dna_strand):
    dna_to_mrna_dict = {"A": "U", "T": "A", "C": "G", "G": "C"}
    return "".join([dna_to_mrna_dict[c] for c in dna_strand])


print(dna_to_mrna("ATACGA")) # UAUGCU
print(dna_to_mrna("CCGTA")) # GGCAU
print(dna_to_mrna("TTACGAGGTCCAGAATCAGTGACCATG")) # AAUGCUCCAGGUCUUAGUCACUGGUAC