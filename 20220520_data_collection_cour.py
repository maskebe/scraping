#Utilisation filtre
#Utilisation Map

import math

#Créer une liste
Liste = [x for x in range(1, 11)]

def pair(x):
    if x % 2 == 0:
        return x

def impair(x):
    if x % 2 != 0:
        return x

def multBy2(x):
    return x * 2

def pow2(x):
    return math.pow(2)

def method1(Liste: list):
    ListePair = []
    ListeImpair = []
    for x in Liste:
        if x % 2 == 0:
            ListePair.append(x)
        else:
            ListeImpair.append(x)
    return ListePair, ListeImpair

def method2(Liste: list):
    ListePair = [x for x in Liste if x % 2 == 0]
    ListeImpair = [x for x in Liste if x % 2 != 0]
    
def method3(Liste: list) -> tuple:
    ListePair = filter(pair, Liste)
    ListeImpair = filter(impair, Liste)
    return list(ListePair), list(ListeImpair)


def methodMap1(Liste: list) -> list:
    result = []

    for x in Liste:
        result.append(x*2)

    return result

def methodMap2(Liste: list) -> list:
    return [x * 2 for x in Liste]

def methodMap3(Liste: list) -> list:
     result = list(map(multBy2, Liste))
     return result

def methodMap4(Liste: list, func) -> list:
     return list(map(func, Liste))

ListeT = [
    [1, 2, 3],
    [4, 5, 6]
]

flatlist = []

for item in ListeT:
    for x in item:
        flatlist.append(x)

print(list(filter(pair, flatlist)))

if __name__== '__main__':
    print(methodMap4(Liste, multBy2))
    print('\n')
    print(methodMap3(Liste))
 #   print('\n')
 #   print(method2(Liste))