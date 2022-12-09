def minion_game(string):
    # your code goes here
    vocales= 'AEIOU'
    puntos_kevin=0
    puntos_stuart=0
    string='BANANA'
    #Kevin crea palabras comienzan con vocales
    for i in range(len(string)):
        if string[i] in vocales:
            puntos_kevin+=len(string)-i
    #Stuart crea palabras comienzan con consonantes
    for i in range(len(string)):
        if string[i] not in vocales:
            puntos_stuart+=len(string)-i


