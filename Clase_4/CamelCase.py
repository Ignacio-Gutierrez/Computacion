s = input()

def camelcase(s):
    # Write your code here
    indice = 0
    palabra = 1
    while indice < len(s):
        letra = s[indice]
        indice += 1
        if letra.isupper() == True:
            palabra += 1
    return palabra
    

print(camelcase(s))
