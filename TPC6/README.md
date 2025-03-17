# TPC6

Para este tpc:
1. Adicionar o botão "Pesquisar" na *navbar*;
2. Fazer o botão "Pesquisar" funcionar;
3. Rota para "Pesquisar";
4. Quando clicamos no botão "Pesquisar", fazer aparecer a entrada correspondente que será o conceito;
5. Dar **bold** onde houver *match* e que este seja clicável, aparecendo sempre a palavra inteira


#TPC AULA 6: fazer o botao pesquisar funcionar - quando carregamos no pesquisar (ou adicionar na navbar), rota para pesquisar
    #e uma nova pagina para pesquisar com um botao PESQUISAR e uma caixa de texto.
    #quando carregamos no botao pesquisar aparece a entrada correspondente que sera o conceito
    #EXTRA: dar bold onde houve match , ou seja ao conceito pesquisado e que seja clicavel (fazer ancora href)
    #tem de aparecer a palavra inteira, nao meias palavras


## Modo de Resolução:

Inicialmente para adicionar o botão "Pesquisar" na *navbar*, foi inserido a seguinte âncora no ficheiro ```layout.html```:
```<a class="nav-link" href="/conceitos">Pesquisar</a>``` (alterar aqui a rota) 
   

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

