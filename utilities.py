import math


def euclidian_norme(x):
    somme = 0
    for elem in x:
        somme += elem**2
    return math.sqrt(somme)


def normalize_vec(x):
    norme = euclidian_norme(x)
    return [elem/norme for elem in x]

