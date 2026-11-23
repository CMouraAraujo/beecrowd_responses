tipo_cha = int(input())
analistas = map(int, input().split())
quantidade_acertos = [1 for analista in analistas if analista == tipo_cha]
print(len(quantidade_acertos))