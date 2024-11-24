# String de entrada
string = "bacdfez"

# Ordenar a string
string_ordenada = ''.join(sorted(string.replace(" ", "")))

# Dividir em grupos consecutivos com tamanho máximo de 3
grupos = []
grupo_atual = string_ordenada[0]

for i in range(1, len(string_ordenada)):
    if len(grupo_atual) == 3 or ord(string_ordenada[i]) != ord(grupo_atual[-1]) + 1:
        grupos.append(grupo_atual)
        grupo_atual = string_ordenada[i]
    else:
        grupo_atual += string_ordenada[i]

# Adicionar o último grupo
grupos.append(grupo_atual)

print(grupos)
