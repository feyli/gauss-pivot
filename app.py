## PARTIE 1.1 ##

# 1.
def permutation(S, i_1, i_2) :
    S[i_1], S[i_2] = S[i_2], S[i_1]
    return S

# 2.
def dilatation(S, i, x) :
    S[i] = [e * x for e in S[i]]
    return S

# 3.
def transvection(S, i_1, i_2, x) :
    a = [e * x for e in S[i_2]]
    S[i_1] = [S[i_1][i] + a[i] for i in range(len(a))]
    return S


## PARTIE 1.2 ##

# 1.
def est_membre_gauche_nul(E):
    return not sum([e != 0 for e in E[:-1]])

#print(est_membre_gauche_nul([0,0,0,0,5]))

# 2.
def ligne_a_simplifier(S):
    for i in range(len(S)):
        if est_membre_gauche_nul(S[i]):
            return i
    return -1
            

# 3.
def simplifier(S):
    for E in S:
        if est_membre_gauche_nul(E) and E[-1] != 0:
            return False
    S = [E for E in S if not est_membre_gauche_nul(E) and E[-1] == 0]
    return True
        

## PARTIE 1.3 ##
# 1.
def coordonnees_pivot(S, k):
    ligne = k
    minimum = -1  # Initialize minimum with a value that will always be updated.
    
    # Ensure you do not go out of bounds by limiting the range
    for i in range(ligne, len(S)):
        for j, val in enumerate(S[i]):
            if val != 0:
                if minimum == -1 or j < minimum:
                    minimum = j
                    ligne = i
                break

    return [ligne, minimum]


S = [[1,-1,1,-1,2],[0,2,1,-3,1],[0,0,0,4,3],[0,0,5,5,-10],[0,0,1,2,2]]
assert coordonnees_pivot(S, 2) == [3, 2], "Erreur dans la fonction coordonnees_pivot"


# 2.
def pivoter(S,k):
    coordonnees = coordonnees_pivot(S,k)
    S = permutation(S, coordonnees[0], k)
    for i in range(k + 1, len(S)):
        if S[i][coordonnees[1]] != 0:
            transvection(S, i, coordonnees[0]-1, S[i][coordonnees[1]]/-S[coordonnees[0]-1][coordonnees[1]])
    return S


S = [[1,-1,1,-1,2],[0,2,1,-3,1],[0,0,0,4,3],[0,0,5,5,-10],[0,0,1,2,2]]
assert pivoter(S, 2) == [[1,-1,1,-1,2],[0,2,1,-3,1],[0,0,5,5,-10],[0,0,0,4,3],[0,0,0,1,4]], "Erreur dans la fonction pivoter"

# 3.
def triangulariser(S):
    if not simplifier(S):
        return False

    for k in range(len(S)):
        pivot_ligne, pivot_colonne = coordonnees_pivot(S, k)
        if S[pivot_ligne][pivot_colonne] == 0:
            if est_membre_gauche_nul(S[pivot_ligne]) and S[pivot_ligne][-1] != 0:
                return False
            continue
        S = permutation(S, pivot_ligne, k)
    return S


assert triangulariser([[1,-1,1,-1,2], [0,2,1,-3,1], [0,0,0,4,3], [0,0,5,5,-10], [0,0,1,2,2]]) == [[1,-1,1,-1,2], [0,2,1,-3,1], [0,0,5,5,-10], [0,0,0,4,3],[0,0,0,0,0]], "Erreur dans la fonction triangulariser"


import numpy as np
A = np.array([[-2,1,-1,-1], [2,2,0,-2], [-2,-1,-1,-2], [-2,1,0,-1]])
Y = np.array([[-1], [1], [1], [-1]])
X = np.linalg.solve(A,Y)
print(X)


import sympy as sp
x1, x2, x3, x4 = sp.symbols('x1 x2 x3 x4')
Eq1 = sp.Eq(3*x1 + 4*x2 + 1*x3 + 2*x4, 3)
Eq2 = sp.Eq(6*x1 + 8*x2 + 2*x3 + 5*x4, 7)
Eq3 = sp.Eq(9*x1 + 12*x2 + 3*x3 + 10*x4, 13)
sp.solve([Eq1,Eq2,Eq3],[x1,x2,x3,x4])
