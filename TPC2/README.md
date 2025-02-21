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
Usada a função ```re.sub(r'hello', '*YEP*', line, flags=re.IGNORECASE)``` que substitui todas as correspondências da palavra ```hello``` na *string* ```line``` por a expressão ```*YEP*```. Usada a ```flag``` ```re.IGNORECASE``` para não diferenciar maiúsculas de minúsculas.





