# Ficha de Expressões Regulares 1
# Exercício 1

# Alínea 1.1
# Dada uma linha de texto, define um programa que determina se a palavra "hello" aparece no início da linha.

import re

line1 = "hello world"
line2 = "goodbye world"
line3 = "hi, hello there"

print("Alinea 1.1:", re.match(r'^hello\b', line1))
print(re.match(r'^hello\b', line2))
print(re.match(r'^hello\b', line3))

# Alínea 1.2
# Dada uma linha de texto, define um programa que determina se a palavra "hello" aparece em qualquer posição da linha.

line1 = "hello world"
line2 = "goodbye world"
line3 = "hi, hello there"

print("Alinea 1.2:", re.search(r'\bhello\b', line1))
print("Alinea 1.2:", re.search(r'\bhello\b', line2))
print("Alinea 1.2:", re.search(r'\bhello\b', line3))

# Alínea 1.3
# Dada uma linha de texto, define um programa que pesquisa por todas as ocorrências da palavra "hello" dentro da linha,
# admitindo que a palavra seja escrita com maiúsculas ou minúsculas.

line = "Hello there! Uh, hi, hello, it's me... Heyyy, hello? HELLO!"
print("Alinea 1.3:", re.findall(r'\bhello\b', line, re.IGNORECASE))

# Alínea 1.4
# Dada uma linha de texto, define um programa que pesquisa por todas as ocorrências da palavra "hello" dentro da linha,
# substituindo cada uma por "*YEP*".

line = "Hello there! Uh, hi, hello, it's me... Heyyy, hello? HELLO!"
print("Alinea 1.4:", re.sub(r'hello', '*YEP*', line, flags=re.IGNORECASE))

# Alínea 1.5
# Dada uma linha de texto, define um programa que pesquisa por todas as ocorrências do caracter vírgula, separando cada
# parte da linha por esse caracter.

line = "bananas, laranjas, maçãs, uvas, melancias, cerejas, kiwis, etc."
print("Alinea 1.5:", re.split(r',\S', line))


# Exercício 2
# Define a função palavra_magica que recebe uma frase e determina se a mesma termina com a expressão "por favor",
# seguida de um sinal válido de pontuação.

def palavra_magica(frase):
    return re.search(r'\bpor favor[!?.,]', frase, re.IGNORECASE)


print("Exercício 2:", palavra_magica("Posso ir à casa de banho, por favor?"))
print(palavra_magica("Preciso de um favor."))


# Exercício 3
# Define a função narcissismo que calcula quantas vezes a palavra "eu" aparece numa string.

def narcissismo(linha):
    return len(re.findall(r'\beu\b', linha, re.IGNORECASE))


print("Exercício 3:",
      narcissismo("Eu não sei se eu quero continuar a ser eu. Por outro lado, eu ser eu é uma parte importante "
                  "de quem EU sou."))


# Exercício 4
# Define a função troca_de_curso que substitui todas as ocorrências de "LEI" numa linha pelo nome do curso dado à função.

def troca_de_curso(linha, novo_curso):
    return re.sub(r'LEI', novo_curso, linha)


print("Exercício 4:", troca_de_curso("LEI é o melhor curso! Adoro LEI! Gostar de LEI devia ser uma lei.", "Biomédica"))


# Exercício 5
# Define a função soma_string que recebe uma string com vários números separados por uma vírgula (e.g., "1,2,3,4,5") e
# devolve a soma destes números.

def soma_string(linha):
    total = map(int, re.split(r',', linha))
    return sum(total)


print("Exercício 5:", soma_string("4,-6,2,3,8,-3,0,2,-5,1"))


# Exercício 6
# Define a função pronomes que encontra e devolve todos os pronomes pessoais presentes numa frase, i.e., "eu", "tu",
# "ele", "ela", etc., com atenção para letras maiúsculas ou minúsculas.

def pronomes(frase):
    return re.findall(r'\b(eu|tu|ele|ela|nós|vós|eles|elas)\b', frase, re.IGNORECASE)


print("Exercício 6:", pronomes("Quando eu fui a Itália, tu foste a França. Depois, eles foram para Espanha sem nós. "
                              "Então ela decidiu que todas elas fossem a Espanha também."))


# Exercício 7
# Define a função variavel_valida que recebe uma string e determina se a mesma é um nome válido para uma variável,
# ou seja, se começa por uma letra e apenas contém letras, números ou underscores.

def variavel_valida(string):
    return re.match(r'\b[a-zA-Z]\w*', string, re.IGNORECASE)


print("Exercício 7:", variavel_valida("Quando eu fui a Itália."))
print("Exercício 7:", variavel_valida("tu foste a123 França"))
print("Exercício 7:", variavel_valida("1Depois, eles foram."))
print("Exercício 7:", variavel_valida("-Então_ela decidiu que todas elas fossem"))


# Exercício 8
# Define a função inteiros que devolve todos os números inteiros presentes numa string. Um número inteiro pode conter
# um ou mais dígitos e pode ser positivo ou negativo.

def inteiros(string):
    return re.findall(r'-?\b\d+\b', string)


print("Exercício 8:", inteiros("1, 0,5, -10, -9,6, 3, 5, 45, 4,5, -7,3"))


# Exercício 9
# Define a função underscores que substitui todos os espaços numa string por underscores. Se aparecerem vários espaços
# seguidos, devem ser substituídos por apenas um underscore.

def underscores(string):
    return re.sub('\s+', '_', string)


print("Exercício 9:", underscores("   Exercicio nove do tpc2 de processamento linguagem natural em engenharia biomédica   ."))


# Exercício 10
# Define a função codigos_postais que recebe uma lista de códigos postais válidos e divide-os com base no hífen.
# A função deve devolver uma lista de pares.

def codigos_postais(lista):
    return [re.split(r'-', codigo) for codigo in lista]


print("Exercício 10:", codigos_postais(["4940-530", "4990-200", "4935-120"]))
