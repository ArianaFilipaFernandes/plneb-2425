# TPC3

Nesta pasta encontra-se o ficheito TPC3.py que é o código desenvolvido para gerar um dicionário médico limpo e organizado em formato ```.txt``` a partir de um ficheiro PDF. 

## Modo de Resolução:

Inicialmente foi necessário recorrer à Shell para que com o comando ```pdftotext``` se converte-se o ficheiro PDF num ficheito ```.txt```.

Depois, no ficheiro aula3_2.py, desenvolveu-se o código que permitiu organizar todo o ficheiro e, no final, gerar um novo ficheiro em formato HTML.

Com a seguinte parte de código, abriu-se o ficheiro para poder ser trabalhado.
```
import re

file = open("../data/dicionario_medico.txt", encoding="utf-8")
texto = file.read()
```

Depois, foi usado ```texto = re.sub(r"\f", "", texto)``` para substituir no ficheiro as quebras de páginas, representadas pela expressão regular ```r"\f"```, por um espaço em branco. De forma a marcar o início de cada parágrafo, substituiu-se duas quebras de linha pelo caractere ```@``` - ```texto = re.sub(r"\n\n", "\n\n@", texto)```.

Com a função ```def limpa_descricao(descricao)``` pretende-se remover espaços extras no início e no fim da string e depois substituir todas as quebras de linha por um espaço. 

Para extrair conceitos implementou-se a seguinte parte do código, que usa a expressão regular ```re.findall```para encontrar todas as ocorrências de conceitos.
```
conceitos_raw = re.findall(r"@(.*)\n([^@]*)", texto)

conceitos = [(designacao, limpa_descricao(descricao)) for designacao, descricao in conceitos_raw]

print(conceitos)
```

**Expressão Regular:** ```r"@(.*)\n([^@]*)"``` - O caractere ```@``` define o início de um conceito e com o ```.```e o ```*``` captura-se tudo até ao final da linha. Com ```\n``` exige-se uma quebra de linha após o conceito e ```([^@]*)```vai capturar a descrição do conceito até encontrar novamente o caractere ```@```.


#### Gerar HTML
Para gerar o ficheiro HTML, criou-se a função ```def gera_html(conceitos)```. 




