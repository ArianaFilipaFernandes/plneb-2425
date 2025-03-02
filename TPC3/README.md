# TPC3

Nesta pasta encontra-se o ficheito TPC3.py que é o código desenvolvido para gerar um dicionário médico limpo e organizado em formato ```.txt``` a partir de um ficheiro PDF. 

## Modo de Resolução:

Inicialmente foi necessário recorrer à Shell para que com o comando ```pdftotext``` se converte-se o ficheiro PDF num ficheito ```.txt```.

Depois, no ficheiro aula3_2.py, desenvolveu-se o código que permitiu organizar todo o ficheiro e, no final, geral um novo ficheiro em formato HTML.

Com a seguinte parte de código, abriu-se o ficheiro para poder ser trabalhado.
```
import re

file = open("../data/dicionario_medico.txt", encoding="utf-8")
texto = file.read()
```

Depois, foi usado ```texto = re.sub(r"\f", "", texto)``` para substituir no ficheiro as quebras de páginas, representadas pela expressão regular ```r"\f"``` por um espaço em branco. De forma a marcar o início de cada parágrafo, substitui-se duas quebras de linha por o caractere ```@``` - ```texto = re.sub(r"\n\n", "\n\n@", texto)```.
