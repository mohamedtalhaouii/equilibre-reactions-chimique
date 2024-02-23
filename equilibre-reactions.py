#ChimeLib Libary #Mohamed Talhaoui
from chemlib import Compound, Reaction


#Les Reactifs
R = int(input("\nCombien des réactifs : "))
A = []
for i in range(1, R + 1):
    A.append(Compound(input("Entrer la molécule "+ str(i) + ": " )))


#Les Produits
P = int(input("Combien des produites : "))
B = []
for i in range(1, P + 1):
    B.append(Compound(input("Entrer la molécule "+ str(i) + ": ")))


#La Reaction
r = Reaction(A , B)
print("\n",r.formula)
NON = r.formula


#La Reaction Correct
if r.is_balanced == False:
    r.balance()
print("\nLa réaction équilibrée de cette équation (", NON, ") est :")
print(r.formula)

