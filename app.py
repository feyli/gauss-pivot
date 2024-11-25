
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
    return sum(E[:-1]) == 0

print(est_membre_gauche_nul([0,0,0,0,5]))

# 2.
def ligne_a_simplifier(S):
    for i in range(len(S)):
        if est_membre_gauche_nul(S[i]):
            return i
    return -1
            

# 3.
def simplifier(S):
    ...

## PARTIE 1.3 ##

# 1.
def coordonnees_pivot(S,k):
    ...

# 2.
def pivoter(S,k):
    ...

# 3.
def triangulariser(S):
    ...
    



    

