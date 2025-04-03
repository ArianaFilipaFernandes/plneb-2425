# TPC8

Objetivo: Consultar o html do content e extrair por categorias todos os elementos do html (ex sintomas, causas...) e adicionar ao json de forma estruturada.


## Modo de Resolução:

Inicialmente foi criada a função ```def get_infos_completas(html_infos)``` que permite extrair as informações das doenças de forma seccionada da página [Atlas da Saúde](https://www.atlasdasaude.pt/doencasAaZ). Para criar esta função, foi necessário consultar os padrões das secções pretendidas, no *content* do html. A *tag* ```<h2>```identifica os títulos: causas, sintomas, tratamento e artigos relacionados. A *tag* ```<h3>``` identifica os títulos dentro dos artigos relacionados e a *tag* ```<p>``` identifica cada parágrafo da secção. 

