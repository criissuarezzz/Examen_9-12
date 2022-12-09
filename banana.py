def minion_game():
    # your code goes here
    vocales= 'AEIOU'
    puntos_kevin=0
    puntos_stuart=0
    string=input('Introduce una palabra: ')
    #Kevin crea palabras comienzan con vocales
    for i in range(len(string)):
        if string[0] in vocales:
            #Se puede formar una palabra que empiece con cualquier vocal del string
            print("kevin ha formado la palabra", string[0:i+1], "suma 1 punto")
            puntos_kevin+=1

    #Stuart crea palabras comienzan con consonantes
    for i in range(len(string)):
        if string[0] not in vocales:
            print("Stuart ha formado la palabra", string[0:i+1], "suma 1 punto")
            puntos_stuart+=1
    if puntos_kevin>puntos_stuart:
        print('Kevin ha gando con', puntos_kevin, 'puntos')
    elif puntos_kevin<puntos_stuart:
        print('Stuart ha gando con', puntos_stuart, 'puntos')
    else:
        print('Empate')

minion_game()

