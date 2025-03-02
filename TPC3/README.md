# TPC3

Nesta pasta encontra-se o ficheito TPC3.py que é o código desenvolvido para gerar um dicionário médico limpo e organizado em formato ```.txt``` a partir de um ficheiro PDF. 
Consta também o ficheiro HTML originado pelo código desenvolvido: dicionario_medico.html.

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


### Gerar HTML
Para gerar o ficheiro HTML, criou-se a função ```def gera_html(conceitos)```. 
```
def gera_html(conceitos):
       html_header = f"""
              <!DOCTYPE html>
              <head>
              <meta charset="UTF-8"/>
              </head>
              <body>  
              <h3>Dicionário de conceitos Médicos</h3>
              <p>Este dicionário foi desenvolvido para a aula de PLNEB 2024/2025</p>"""
       html_conceitos = ""
       for designacao, descricao in conceitos:
              html_conceitos += f"""
                            <div>
                            <p><b>{designacao}</b></p>
                            <p>{descricao}</p>
                            </div>
                            <hr/>
                     """

       html_footer = """
                     </body>
              </html>"""
       return html_header + html_conceitos + html_footer
```

Definiu-se o tipo de documento - ```<!DOCTYPE html>```. Com ```<meta charset="UTF-8"/>``` garante-se suporte para caracteres com acentuação.
O título do documento definiu-se com ```<h3>``` e a descrição do documento com ```<p>```.
Depois criou-se um ciclo ```for``` que percorre a lista ```conceitos``` e adiciona ao documento HTML da seguinte forma: ```<p>``` em negrito (```<b>```) para o nome do conceito e novamente um ```<p>``` para a descrição do conceito. Por fim, ```<hr/>``` para separar os conceitos.

No final, fecha-se o HTML (```html_footer =```)

```return html_header + html_conceitos + html_footer``` junta todas as partes do HTML. 

------------------------------
