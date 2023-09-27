chave = input('Digite a base da sua senha:')
senha = ""

for letra in chave:
    if letra in "Aa":
        senha = senha + "@"
    elif letra in "Bb":
        senha = senha + "11"
    elif letra in "Cc":
        senha = senha + "12"
    elif letra in "Dd":
        senha = senha + "13"
    elif letra in "Ee":
        senha = senha + "14"
    elif letra in "Ff":
        senha = senha + "15"
    elif letra in "Ss":
        senha = senha + "*"
    elif letra in "Ii":
        senha = senha + "1"
    elif letra in "Rr":
        senha = senha + "#"
    elif letra in "Oo":
        senha = senha + "0"
    elif letra in "Uu":
        senha = senha + "u.u"
    else: 
        senha = senha + letra
print(senha)     
