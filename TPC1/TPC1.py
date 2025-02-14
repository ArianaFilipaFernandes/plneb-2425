# Create a function that:

# 1: given a string "s", reverse it.

s = "TPC1 de PLN em EngBiom"
def reverse_string(s):
    return s[::-1]

result1 = reverse_string(s)
print(result1)

# 2: given a string "s", returns how many "a" and "A" characters are present in it.
def characters(s):
    return s.upper().count("A")

result2 = characters(s)
print(result2)

# 3: given a string "s", returns the number of vowels there are present in it.
def count_vowels(s):
    vowels = "AEIOU"
    s = s.upper()
    return sum(s.count(vowel) for vowel in vowels)

result3 = count_vowels(s)
print(result3)

# 4: given a string "s", convert it into lowercase.

def lowercase(s):
    return s.lower()

result4 = lowercase(s)
print(result4)

# 5: given a string "s", convert it into uppercase.
def uppercase(s):
    return s.upper()

result5 = uppercase(s)
print(result5)

# 6: Verifica se uma string é capicua.

def capicua(s):
    if s[0:] == s[::-1]:
        return True
    else:
        return False

result6 = capicua(s)
print(result6)

# 7: Verifica se duas strings estão balanceadas (Duas strings, s1 e s2, estão balanceadas se todos os caracteres de s1 estão presentes em s2.
s1 = "Processamento de Linguagem Natural"
s2 = "Engenharia Biomédica"

def balanceadas(s1, s2):
    return all(char in s2 for char in s1)

print(balanceadas(s1,s2))

# 8: Calcula o número de ocorrências de s1 em s2.

def num_ocorrencias(s1, s2):
    return s2.count(s1)

result7 = num_ocorrencias(s1,s2)
print(result7)

# 9: Verifica se s1 é anagrama de s2 ("listen" e "silent" deve imprimir True | "hello" e "world" deve imprimir False).
def anagrama(s1, s2):
    return sorted(s1) == sorted(s2)

result8 = anagrama(s1,s2)
print(result8)

# 10: Dado um dicionário, calcular a tabela das classes de anagramas.

dic = {"amor": "roma", "praia": "brasil", "calma": "malta", "beleza": "florença"}
def tabela_anagrama(dic):
    dic1 = {}

    for word, value in dic.items():
        key_word = "".join(sorted(word))
        key_value = "".join(sorted(value))

        if key_word == key_value:
            if key_word not in dic1:
                dic1[key_word] = [word, value]
            else:
                dic1[key_word].extend([word, value])

    return dic1

result9 = tabela_anagrama(dic)

for key_word, key_value in result9.items():
    print(f"Classe {key_word}: {set(key_value)}")
    print(f"Classe {key_word}: {set(key_value)}")

