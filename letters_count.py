string = "bacdfez"
string_ordenada = ''.join(sorted(string.replace(" ", "")))

grupos, grupo_atual = [], string_ordenada[0]
for i in string_ordenada[1:]:
    if len(grupo_atual) == 3 or ord(i) != ord(grupo_atual[-1]) + 1:
        grupos.append(grupo_atual)
        grupo_atual = i
    else:
        grupo_atual += i
grupos.append(grupo_atual)

print(grupos)
