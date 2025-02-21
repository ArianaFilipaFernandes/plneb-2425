# TPC2

Nesta pasta encontra-se o ficheito TPC2.py que é o código desenvolvido para o trabalho de casa pedido na segunda aula. 
Este tpc é composto por várias alíneas e exercícios que estão devidamente identificados ao longo do código presente no ficheiro TPC2.py.

### Modo de Resolução:
**Alínea 1.1** - usada a função ```re.match()``` que analisa a ```string``` e tenta encontrar uma correspondência para a expressão regular ```r'^hello\b'``` a partir do início da ```string```, devolvendo ```None```se não encontrar nenhuma. 

***Expressão Regular:*** ```r'^hello\b'```- ```^``` usado para confirmar se o padrão ocorre no início da linha; ```hello``` é a palavra pedida para encontrar; ```\b``` *word boundary* para limitar o fim da palavra. 

re.match(pattern, string[, flags]) - analisa a string e tenta encontrar uma correspondência para a expressão regular pattern a partir do início da string. Devolve None se não encontrar nenhuma correspondência.

Para o exercício 7 surgiu a necessidade de criar duas novas *strings* - **s1 = "Processamento de Linguagem Natural"** e **s2 = "Engenharia Biomédica"** usadas nos exercícios 7, 8 e 9.

- Exercício 7 - foi criada a função ```def balanceadas(s1, s2)```. Esta função percorre cada caractere em **s1** e verifica se está em **s2**, retornando ```True```se todos os caracteres de **s1** estiverem presentes na *string* **s2** ou ```False``` caso contrário;
- Exercício 8 - foi criada a função ```def num_ocorrencias(s1, s2)``` que conta quantas vezes **s1** aparece dentro de **s2**;
- Exercício 9 - foi criada a função ```def anagrama(s1, s2)```que ordena ambas as *strings* e compara-as, retornando ```True```se forem anagramas ou ```False``` caso contrário;

Para o exercício 10 foi criado o seguinte dicionário: ```dic = {"amor": "roma", "praia": "brasil", "calma": "malta", "beleza": "florença"}```e a seguinte função: ```def tabela_anagramas(dic)```.  Esta função cria um dicionário vazio para as classes de anagramas e ordena as letras de *word* e *value*. Depois, verifica se as palavras são anagramas e adiciona as que forem.

Para obter os resultados de todos os exercícios, basta fazer o *run* do ficheiro TPC1.py.
