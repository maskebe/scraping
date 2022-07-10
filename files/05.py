import re
from unittest import result

# La plupart des lettres ou caractères correspondent simplement à eux-mêmes.
# Par exemple, l'expression régulière test correspond à la chaîne de caractères test, précisément.
# Vous pouvez activer le mode non-sensible à la casse qui permet à cette RE de correspondre également à Test ou TEST (ce sujet est traité par la suite).
# Il existe des exceptions à cette règle ; certains caractères sont des métacaractères spéciaux et ne correspondent pas à eux-mêmes.
# Au lieu de cela, ils signalent que certaines choses non ordinaires doivent correspondre, ou ils affectent d'autre portions de la RE en les répétant ou en changeant leur sens.
# Une grande partie de ce document est consacrée au fonctionnement de ces métacaractères.
# Voici une liste complète des métacaractères ; leur sens est décrit dans la suite:
#   ^ : Utiliser pour exprimer la négation (SAUF le caractère): [^5] === Tous les caractères sauf 5.
#       Dans le cas ou il est utilisé comme suit: [5^] il est dépourvu de son premier sens.
#       Ainsin dans ce cas on aura tous les caractères (5) et (^).

#   $ : Trouver l'expression à la fin de la chaine de caractère.
#   * : Métacaractère de répétition. Il spécifie que le caractère précédent peut correspondre zéro, une ou plusieurs fois (au lieu d'une seule fois).
#       Par exemple, cha*t correspond à 'cht' (0 caractère 'a'), 'chat' (1 'a'), 'chaaat' (3 caractères 'a') et ainsi de suite.
#       Exemple:  Considérons l'expression a[bcd]*b. Elle correspond à la lettre 'a', suivi d'aucune ou plusieurs lettres de la classe [bcd] et finit par un 'b'.
#   + : Un autre métacaractère de répétition est +, qui fait correspondre une ou plusieurs fois.
#       Pour continuer avec le même exemple, cha+t correspond avec 'chat' (1 'a'), 'chaaat' (3 'a') mais ne correspond pas avec 'cht'.
#   ? : Il existe deux autres quantificateurs pour les répétitions.
#       Le point d'interrogation, ?, fait correspondre zéro ou une fois ; vous pouvez vous le représenter comme indiquant une option.
#   ? : Il existe deux autres quantificateurs pour les répétitions.
#       Le point d'interrogation, ?, fait correspondre zéro ou une fois ; vous pouvez vous le représenter comme indiquant une option.
#       Par exemple, méta-?caractère fait correspondre soit métacaractère, soit méta-caractère.
#   { } : {m,n} ou m represente le minimum et n le maximum.
#         Par exemple, a/{1,3}b fait correspondre 'a/b', 'a//b' et 'a///b'.
#         Elle ne fait pas correspondre 'ab' (pas de barre oblique) ni 'a////b' (quatre barres obliques).
#         Vous pouvez omettre soit m, soit n ; dans ce cas, une valeur raisonnable est prise pour la valeur manquante.
#         Omettre m considère que la borne basse est 0 alors qu'omettre n signifie qu'il n'y a pas de borne supérieure.
#           - {0,} correspond à '*'
#           - {1,} correspond à '+'
#           - {0,1} correspond à '?'
#   [ ] : Utiliser pour trouver un ensemble de caractère.
#         [abc] === [a-c] Tous les caractère de a à c.
#         Ainsi on remarque aisément que (-) signé à ou défini une plage de caractères
#   \ : Utiliser pour soit échapper afin d'annuller la signification spéciale d'un métacaractère.
#       Ou utiliser aussi pour renvoyer des ensembles de caractères bien définis. A savoir:
#           - \w : correspond à n'importe quel caractère alphanumérique.
#               Si l'expression régulière est exprimée en bytes, c'est équivalent à la classe [a-zA-Z0-9_].
#               Si l'expression régulière est une chaîne de caractères, il correspond à tous les caractères identifiés comme lettre dans la base de données Unicode.
#           - \d : Correspond à n'importe quel caractère numérique ; équivalent à la classe [0-9].
#           - \s : Correspond à n'importe quel caractère « blanc » ; équivalent à la classe [ \t\n\r\f\v].
#           - \S : Correspond à n'importe quel caractère autre que « blanc » ; équivalent à la classe [^ \t\n\r\f\v].
#           - \w+: Permet de correspondre a un ensemble de lettres formant un mot ou soit la lettre elle même car \w === (Un caractère ALPHA... Puis le (+) {1,} Pour la formulation du mot)
#           - \S : Correspond à n'importe quel caractère non-alphanumérique ; équivalent à la classe [^a-zA-Z0-9_].


var = "Lorem Lopem Losem example@gmail.com ipsum example@yahoo.fr example@yahoo.com example@hotmail.fr dolor sit amet consectetur adipisicing elit. 777 787654432 78535090 76535090 79615516 +221777778865 +22997532341"

def dividerLine(n=20):
    var = '-' * int(n)
    print(var)
    
    
if __name__ == '__main__':
    dividerLine()
    regex = re.compile('\w+')
    results = re.findall(regex, var)
#print(results)
    
    # Retrouver un mot en particulier
    # Méthode 1
    dividerLine()
   # var1 = re.compile('Lorem')
   # var1 = re.findall(var1, var)
   # print(var1)

    # Retrouver un mot en particulier
    # Méthode 2
    dividerLine()
  #  var1 = re.compile("L[a-z]{1,}m")
   # var1 = re.findall(var1, var)
   # print(var1)

    # Retrouver un mot en particulier
    # Méthode 3
    dividerLine()
   # var1 = re.compile("L[a-z]+m")
   # var1 = re.findall(var1, var)
   # print(var1)

    dividerLine()
    var2 = re.compile("78[0-9]+2")
    var3 = re.findall(var2, var)
    print(var3)

