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

```<a class="nav-link" href="/pesquisar">Pesquisar</a>``` 

Depois foi criada a rota ```/pesquisar```:

```
@app.route("/pesquisar")
def pesquisar():
    return render_template("pesquisar.html")
```

Também foi criado na diretoria ```templates```o ficheiro ```pesquisar.html```.

Foi adaptado o *Form* *Overview* do *bootstrap*:

```
   <form>
        <div class="mb-3">
            <label for="conceito_input" class="form-label">Conceito</label>
            <input type="text" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
            <div id="emailHelp" class="form-text" id="conceito_input">Insira o conceito que pretende pesquisar</div>
        </div>
        <button type="Submit" class="btn btn-primary">Pesquisar conceito</button>
    </form>
``` 

------------------------------

