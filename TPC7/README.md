# TPC7

O objetivo para este tpc é adicionar ao menu uma tabela bem construída, usando um estilo (por exemplo bootstrap 5) e ativar a pesquisa com expressões regulares.

## Modo de Resolução:

1) Inicialmente, ao ficheiro ```tabela.html``` criado na aula denominou-se as colunas de "Designação" e "Descrição" e criou-se um ciclo ```for``` para que a tabela seja preenchida com os dados da base de dados. 

```
{% extends 'layout.html' %}

{% block head %}
<title> Tabela </title>
{% endblock %}

{% block body %}

<table id="tabela_conceitos" class="display">
    <thead>
        <tr>
            <th>Designação</th>
            <th>Descrição</th>
        </tr>
    </thead>
    <tbody>
        {%for designacao, descricao in database %}
            <tr>
                <td>{{ designacao }}</td>
                <td>{{ descricao }}</td>
            </tr>
        {% endfor %}
    </tbody>
</table>

{% endblock %}

```

2) Depois, atualizou-se a rota já criada ```@app.get("/conceitos/tabela")```:

```
@app.get("/conceitos/tabela")
def conceitos_tabela():
    return render_template("tabela.html", database=db.items(), title="Tabela de Conceitos")
```

3) Na ```navbar``` da página foi adicionada a opção "Tabela de Conceitos" para um acesso direto a esta. Para isso, no ficheiro ```layout.html``` foi adicionada a âncora ```<a class="nav-link" href="/conceitos/tabela">Tabela de Conceitos</a>``` dentro do ```body```. 

4) Para ativar a pesquisa com expressões regulares, como sugerido na aula, recorreu-se à página [DataTables] (https://datatables.net/).

   ```
$(document).ready( function () {
    $('#tabela_conceitos').DataTable({
        search: {
        regex: true
    }
    });
});
```
Foi só adicionar a flag ```search: {regex: true}```.










------------------------------
