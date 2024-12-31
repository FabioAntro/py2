def lunghezze_parole(A):
    B = [len(parola) for parola in A]
    return B

A = ["steam", "gift", "card", "bait"]
B = lunghezze_parole(A)
print(B)
