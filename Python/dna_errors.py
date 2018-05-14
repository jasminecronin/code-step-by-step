def dna_errors(dna1, dna2):
    errors = 0
    errors += abs(len(dna1) - len(dna2))
    i = 0
    pom = 0
    while i < len(dna1) and i < len(dna2):
        if dna1[i] == 'A' and dna2[i] != 'T':
            pom += 2
        elif dna1[i] == 'T' and dna2[i] != 'A':
            pom += 2
        elif dna1[i] == 'C' and dna2[i] != 'G':
            pom += 2
        elif dna1[i] == 'G' and dna2[i] != 'C':
            pom += 2
        i += 1
    errors += pom
    errors += dna1.count('-')
    errors -= dna2.count('-')
    return errors
