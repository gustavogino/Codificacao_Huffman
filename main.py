#!/usr/bin/env python
import sys

arquivo = input("Digite o nome do arquivo de texto que deseja codificar: ")

with open(arquivo, 'r') as meu_texto:
	string = meu_texto.read()
	tamanho_original = len(string)


class No_arvore(object):
    def __init__(self, esquerda=None, direita=None):
        self.esquerda = esquerda
        self.direita = direita

    def filhos(self):
        return (self.esquerda, self.direita)

    def nos(self):
        return (self.esquerda, self.direita)

    def __str__(self):
        return "%s_%s" % (self.esquerda, self.direita)


def Codificacao_Huffman(nodo, esquerda=True, string_binaria=""):
    if type(nodo) is str:
        return {nodo: string_binaria}
    (esquerda, direita) = nodo.filhos()
    dicionario = dict()
    dicionario.update(Codificacao_Huffman(esquerda, True, string_binaria + "0"))
    dicionario.update(Codificacao_Huffman(direita, False, string_binaria + "1"))
    return dicionario


frequencia_ordenada = {}
for char in string:
    if char in frequencia_ordenada:
        frequencia_ordenada[char] += 1
    else:
        frequencia_ordenada[char] = 1

frequencia_ordenada = sorted(frequencia_ordenada.items(), key=lambda x: x[1], reverse=True)

nos = frequencia_ordenada

while len(nos) > 1:
    cod1, char1 = nos[-1]
    cod2, char2 = nos[-2]
    nos = nos[:-2]
    nodo = No_arvore(cod1, cod2)
    nos.append((nodo, char1 + char2))

    nos = sorted(nos, key=lambda x: x[1], reverse=True)


Huffman = Codificacao_Huffman(nos[0][0])



print (" ")
print (" TRABALHO DE ALGORITMOS : Gustavo Gino Scotton")
print (" ")
print ("	Letra  |  Frequência  |  Codificação Huffman ")
print (" ")
print ("=================================================")

total = 0

for letra, frequencia in frequencia_ordenada:
    print (" %-4r   |  %5d   |  %12s" % (letra, frequencia, Huffman[letra]))
    total += frequencia * len(Huffman[letra])


print (" COMPARAÇÃO: ")
print (" ")
print ("Tamanho original em bits: ", tamanho_original * 8)
print("Total de bits pós codificação: ",total)    
