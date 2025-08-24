dna = "CGAGCTAGCTCCCGTGCGTGCGCCCTAGCTGTATACCGGCATAACGTGATATCGTACCTTCTAAATAACGGCATACATCACGTGATATCCTTCGTCATCAATCCATCTATATCTAGCCTTATAACGCGCCTTATCCATAACTCCCTAGCGCAATAACTCCATCGCGGACCTTCTAAATCAATCCATCCCTAACGGACTAGATCAATCCATATCCTTATACATCCCCTTCGATCTAGATAAATACATCCATCCATCACGTGATCTCCCGATCACTCCATACATCTAGACATGCATATCTTC"

# Mapping: A=00, C=01, G=10, T=11
mapping = {'A': '00', 'C': '01', 'G': '10', 'T': '11'}

# Split the DNA into chunks of 4
chunk_size = 4
chunks = [dna[i:i+chunk_size] for i in range(0, len(dna), chunk_size)]

# If the last chunk is not full, ignore it
if len(chunks[-1]) < chunk_size:
    chunks = chunks[:-1]

flag = ""
for chunk in chunks:
    # Convert each nucleotide to its binary representation
    bin_str = ''.join(mapping[n] for n in chunk)
    # Convert the binary string to an integer
    num = int(bin_str, 2)
    # Convert the integer to an ASCII character
    flag += chr(num)

print(flag)