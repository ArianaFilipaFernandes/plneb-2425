# TPC5

Para este tpc foi pedido a criação da rota ```conceitos/<designacao>``` que permite fazer um *render template* de um conceito. Foi pedido ainda que mostrasse a designação e a descrição do conceito e, ainda, colocar a lista a ir para a rota do conceito quando clicamos num elemento.

## Modo de Resolução:

1) Ao trabalho já desenvolvido na aula, foi adicionado um ficheiro html de nome "conceito", para que a função ```render_template``` possa usá-lo para preenchê-lo com o nome do conceito (designacao) e a respetiva descrição (descricao).

Depois, foi criada então a rota ```conceitos/<designacao>```:

```
@app.route("/conceitos/<designacao>")
def o_conceito(designacao):
        if designacao in db:
            return render_template("conceito.html", designacao=designacao, descricao=db[designacao])
```

Para verificar o conceito é necessário aceder a (http://localhost:4002/conceitos/vida), em que onde temos a palavra "vida" deverá estar o nome do conceito que pretendemos consultar.

2) Para a segunda parte do tpc, foi necessário alterar o ficheito ```conceitos.html``` com a introdução de links.

A alteração consistiu em acrescentar ```<a href="{{ url_for('o_conceito', designacao=designacao) }}">{{ designacao }}</a>``` na lista dos elementos.

------------------------------

