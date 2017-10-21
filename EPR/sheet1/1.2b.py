def harmonic_series(terms: int) -> float:
    return sum([(-1) ** (k + 1) / k for k in range(1, terms)])


for i in [3, 9, 15]:
    print("Harmonic series (ln(2)) for {:2} terms: {:.4f}".format(i, harmonic_series(i)))
