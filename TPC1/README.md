# TPC1

Nesta pasta encontra-se o ficheito TPC1.py que é o código desenvolvido para o trabalho de casa pedido na primeira aula. 

### Modo de Resolução:
Foi criada uma *string* inicial - **s = "TPC1 de PLN em EngBiom"** - usada até ao exercício 6, inclusive.

- Exercício 1 - foi criada a função ```def reverse_string(s)```. Esta função vai inverter a *string* através do *slicing*;
- Exercício 2 - foi criada a função ```def characters(s)```. Esta função converte para maiúsculas todos os caracteres da *string* e conta os "A";
- Exercício 3 - foi criada a função ```def count_vowels(s)```. Esta função converte a *string* para maiúsculas e soma quantas vogais há na *string*;
- Exercício 4 - foi criada a função ```def lowercase(s)```para converter a *string* em minúsculas;
- Exercício 5 - foi criada a função ```def uppercase(s)```para converter a *string* em maiúsculas;
- Exercício 6 - foi criada a função ```def capicua(s)```. Esta função usa o *slicing* para verificar se a *string* é capicua;

Para o exercício 7 surgiu a necessidade de criar duas novas *strings* - **s1 = "Processamento de Linguagem Natural"** e **s2 = "Engenharia Biomédica"** usadas nos exercícios 7, 8 e 9.

- Exercício 7 - foi criada a função ```def balanceadas(s1, s2)```. Esta função percorre cada caractere em **s1** e verifica se está em **s2**, retornando ```True```se todos os caracteres de **s1** estiverem presentes na *string* **s2** ou ```False``` caso contrário;
- Exercício 8 - foi criada a função ```def num_ocorrencias(s1, s2)``` que conta quantas vezes **s1** aparece dentro de **s2**;
- Exercício 9 - foi criada a função ```def anagrama(s1, s2)```que ordena ambas as *strings* e compara-as, retornando ```True```se forem anagramas ou ```False``` caso contrário;

Para o exercício 10 foi criado o seguinte dicionário: ```dic = {"amor": "roma", "praia": "brasil", "calma": "malta", "beleza": "florença"}```e a seguinte função: ```def tabela_anagramas(dic)```.  Esta função cria um dicionário vazio para as classes de anagramas e ordena as letras de *word* e *value*. Depois, verifica se as palavras são anagramas e adiciona as que forem.

Para obter os resultados de todos os exercícios, basta fazer o *run* do ficheiro TPC1.py.
