from chemlib import Reaction

#N.B
print("\nEntrez des lettres majuscules (A B C), ne pas oublier la flèche (-->)\n ")

#La Formule
M = input("Entrer La Reaction Chimique : \n")
r = Reaction.by_formula(M)

#Equilibre
if r.is_balanced == True:
    print("\n",r.formula)
    
NON = r.formula

#N'est Pas Equilibre
if r.is_balanced == False:
    r.balance()
    print("\nLa réaction équilibrée de cette équation (", NON, ") est :")
    print(r.formula)
