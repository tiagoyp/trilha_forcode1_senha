senha = input('coloque uma senha de 4 dígitos, podendo conter alarismos e letras maiúsculas e minúsculas: ')
alg=['0','1','2','3','4','5','6','7','8','9']
min=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
mai=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

i = 0
temalg = False
temmin = False
temmai = False
if len(senha) == 4:       
    while i < 4:
        if senha[i] in alg:
            temalg = True
        elif senha[i] in mai:
            temmai = True
        elif senha[i] in min:
            temmin = True
        i += 1
    if temalg and temmin and temmai:
        print('senha forte')
    elif (temalg and temmin) or (temalg and temmai) or (temmai and temmin):
        print('senha media')
    else:
        print('senha fraca')
else:
    print('por favor digite 4 digitos')