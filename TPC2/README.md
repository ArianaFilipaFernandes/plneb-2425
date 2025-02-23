# TPC2

Nesta pasta encontra-se o ficheito TPC2.py que é o código desenvolvido para o trabalho de casa pedido na segunda aula. 
Este tpc é composto por várias alíneas e exercícios que estão devidamente identificados ao longo do código presente no ficheiro TPC2.py.

## Modo de Resolução:
### Alínea 1.1: 
Usada a função ```re.match()``` que analisa a ```string``` e tenta encontrar uma correspondência para a expressão regular ```r'^hello\b'``` a partir do início da ```string```, devolvendo ```None```se não encontrar nenhuma. 

***Expressão Regular:*** ```r'^hello\b'```- ```^``` usado para confirmar se o padrão ocorre no início da linha; ```hello``` é a palavra pedida para encontrar; ```\b``` *word boundary* para limitar o fim da palavra. 


### Alínea 1.2: 
Usada a função ```re.search()``` que analisa a ```string``` e tenta encontrar uma correspondência para a expressão regular ```r'\bhello\b'``` em qualquer posição da ```string```, devolvendo ```None```se não encontrar nenhuma. 

***Expressão Regular:*** ```r'\bhello\b'```- usado ```\b``` no início e no fim da palavra ```hello``` para encontrar exatamente a correspondência desta, sem nada antes, nem depois.


### Alínea 1.3: 
Usada a função ```re.findall()``` que encontra todas as correspondênciasda palavra ```hello``` na ```string``` e devolve uma lista. Usada a ```flag``` ```re.IGNORECASE``` para não diferenciar maiúsculas de minúsculas.

***Expressão Regular:*** ```r'\bhello\b'```- usado ```\b``` no início e no fim da palavra ```hello``` para encontrar exatamente a correspondência desta, sem nada antes, nem depois.


### Alínea 1.4: 
Usada a função ```re.sub(r'hello', '*YEP*', line, flags=re.IGNORECASE)``` que substitui todas as correspondências da palavra ```hello``` na *string* ```line``` pela expressão ```*YEP*```. Usada a ```flag``` ```re.IGNORECASE``` para não diferenciar maiúsculas de minúsculas.


### Alínea 1.5: 
Usada a função ```re.split``` divide a *string* com base nas correspondências da expressão regular ```r',\S'```.

***Expressão Regular:*** ```r',\S'```- colocado o caractere ',' para procurar por ele mesmo e ```\S``` para a vírgula ser seguida por um caractere que não seja um espaço em branco.


### Exercício 2: 
Definida a seguinte função: ```def palavra_magica(frase)``` que usa a função ```re.search``` para procurar se a expressão regular ```r'\bpor favor[!?.,]'``` está dentro da ```frase```.

***Expressão Regular:*** ```r'\bpor favor[!?.,]'``` - usado *word boundary* para que 'por favor' seja uma palavra completa e definidos os caracteres considerados sinais válidos de pontuação dentro dos parêntesis retos. Colocada ainda a ```flag``` ```re.IGNORECASE``` para não diferenciar maiúsculas de minúsculas.


### Exercício 3: 
Definida a seguinte função: ```def narcissismo(linha)``` que usa a função ```re.findall``` para encontrar a expressão regular ```r'\beu\b'``` na *string*. Usado ```len()``` para contar as vezes que a palavra 'eu' aparece.

***Expressão Regular:*** ```r'\beu\b'``` - usado *word boundary* para que 'eu' seja uma palavra completa. Colocada ainda a ```flag``` ```re.IGNORECASE``` para não diferenciar maiúsculas de minúsculas.


### Exercício 4: 
Definida a seguinte função: ```def troca_de_curso(linha, novo_curso)``` que usa a função ```re.sub``` que vai substituir a palavra 'LEI' pelo nome do novo curso  na *string*.


### Exercício 5: 
Definida a seguinte função: ```def soma_string(linha)``` que usa a função ```re.split``` para dividir a *string* sempre que encontrar uma vírgula. Como devolve uma lista de *strings* foi usado ```map(int...)``` para converter a lista de *strings* em lista de números inteiros. Para obter a soma dos números foi usado ```sum()```.


### Exercício 6: 
Definida a seguinte função: ```def pronomes(frase)``` que usa a função ```re.findall``` para encontrar a expressão regular ```r'\b(eu|tu|ele|ela|nós|vós|eles|elas)\b'``` na *string*. Colocada a ```flag``` ```re.IGNORECASE``` para não diferenciar maiúsculas de minúsculas.

***Expressão Regular:*** ```r'\b(eu|tu|ele|ela|nós|vós|eles|elas)\b'``` - usado *word boundary* para que os pronomes sejam palavras completas e não parte de outras. 


### Exercício 7: 
Definida a seguinte função: ```def variavel_valida(string)``` que usa a função ```re.match``` que analisa a *string* e tenta encontrar uma correspondência para a expressão regular ```r'\b[a-zA-Z]\w*'``` a partir do início da ```string```, devolvendo ```None```se não encontrar nenhuma. 

***Expressão Regular:*** ```r'\b[a-zA-Z]\w*'``` - usado *word boundary* para que sejam palavras completas e não parte de outras. Definido dentro de parêntesis retos que o primeiro caractere deve ser uma letra maiúscula ou minúscula e com ```\w*``` garante-se que depois da primeira letra pode haver mais letras, números inteiros ou *underscore*.


### Exercício 8: 
Definida a seguinte função: ```def inteiros(string)``` que usa a função ```re.findall``` para encontrar a expressão regular ```r'-?\b\d+\b'``` na *string*

***Expressão Regular:*** ```r'-?\b\d+\b'``` - Algumas dificuldades nesta expressão regular, pelo que o *output* obtido não é o correto, no entanto, o objetivo era que com ```-?``` pudessem ser considerados números negativos ou positivos, pois ```-``` poderia aparecer 0 ou 1 vez. Depois colocado *word boundary* antes e depois de ```\d+```, para que pudessem ser um ou mais dígitos.


### Exercício 9: 
Definida a seguinte função: ```def underscores(string)``` que usa a função ```re.sub``` que vai substituir a expressão regular ```r'\s+'```` por *underscores* na *string*.

***Expressão Regular:*** ```r'\s+'`` - Considera todos os todos os espaços em branco uma ou mais vezes. 


### Exercício 10: 
Definida a seguinte função: ```def codigos_postais(lista)``` que usa a função ```re.split``` para dividir a *string* sempre que encontrar um hífen. Na expressão regular é definido o caractere '-'. Usado o *loop* ```for``` percorre cada código postal separadamente e aplica a função ```re.split```.

