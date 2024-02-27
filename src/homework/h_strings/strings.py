def get_hamming_distance(dna1,dna2):
    #Logic to get the hamming distance
    if len(dna1) != len(dna2):
        raise ValueError("DNA strings must have equal length")
    distance = 0
    for i in range(0,len(dna1)-1):
        if dna1[i] != dna2[i]:
            distance+=1
    return distance

def get_dna_complement(dna):
    """Return the reverse complement of the DNA string s."""
    # Mapping of letters to their complements
    dna = dna.upper()
    complement_map = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    
    # Reverse the input string and replace each letter with its complement
    reverse_dna = ''.join(complement_map[i] for i in dna[::-1])
    
    return reverse_dna

# # Example usage
# dna_string = "GTCA"
# reverse_comp_dna = get_dna_complement(dna_string)
# print(f"The reverse complement of '{dna_string}' is '{reverse_comp_dna}'.")
