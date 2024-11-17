from collections import Counter

string = "Domingo estamos de folga"

string_sem_espaco = string.replace(" ", "")

frequencia = Counter(string_sem_espaco)

letras_ordenadas = sorted(frequencia.items(), key=lambda x: (-x[1], x[0]))

