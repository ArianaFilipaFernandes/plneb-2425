# Introdução ao beautifulsoup
import json
from bs4 import BeautifulSoup
import requests

#---------------------TPC8--------------------
def get_infos_completas(html_infos):
    soup = BeautifulSoup(html_infos, "html.parser")

    infos_completas = {
    'causas': '',
    'sintomas': [],
    'tratamento': '',
    'artigos_relacionados': [],
    'nota': ''
    }
    # Causas
    info_causas = soup.find('h2', string='Causas')
    if info_causas:
        causas_text = info_causas.find_next('p').get_text(strip=True)
        infos_completas['causas'] = causas_text

    # Sintomas
    info_sintomas = soup.find('h2', string='Sintomas')
    if info_sintomas:
        sintomas_list = info_sintomas.find_next('ul')  # Em lista
        if sintomas_list:
            infos_completas['sintomas'] = [li.get_text(strip=True) for li in sintomas_list.find_all('li')]

    # Tratamento
    info_tratamento = soup.find('h2', string='Tratamento')
    if info_tratamento:
        tratamento_text = info_tratamento.find_next('p').get_text(strip=True)
        infos_completas['tratamento'] = tratamento_text

    # Artigos Relacionados
    info_artigos_relacionados = soup.find('h2', string='Artigos Relacionados')
    if info_artigos_relacionados:
        artigos_relacionados_list = info_artigos_relacionados.find_next('h3').find_all('a')
        if artigos_relacionados_list:
            infos_completas['Artigos Relacionados'] = [a['href'] for a in artigos_relacionados_list]

    return infos_completas

def get_doenca_info(url_href):
    url_doenca = "https://www.atlasdasaude.pt" + url_href
    response = requests.get(url_doenca)
    html_content = response.text
    soup = BeautifulSoup(html_content, "html.parser")

    div_content = soup.find("div", class_ ="node-doencas")

    date = div_content.find("div", class_="field-name-post-date").div.div.text #Data
    desc = div_content.find("div", class_="field-name-body").div.div.text #Descrição
    note = div_content.find("div", class_="field-name-field-nota")

    note_text = note.find("div", class_="field-item even").text.strip() if note else ""

    # Outras infos
    info = div_content.find("div", class_="field-name-body").div.div
    sections = get_infos_completas(str(info))

    return {
        "url": url_doenca,
        "data": date,
        "descricao": desc,
        "causas": sections["causas"],
        "sintomas": sections["sintomas"],
        "tratamento": sections["tratamento"],
        "artigos_relacionados": sections["artigos_relacionados"],
        "nota": note_text
    }

def doencas_letra(letra):
    url = "https://www.atlasdasaude.pt/doencasAaZ/" + letra
    print(url)
    response = requests.get(url)

    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')

# No teste é comum sair uma pergunta de beautifulsoup. É importante fazera estrutura toda: div-div-h3-a (verificar estrutura)
    doencas = {}
    for div_row in soup.find_all('div', class_='views-row'):
        designacao = div_row.div.h3.a.text.strip()
        doenca_url = div_row.div.h3.a["href"]
        doenca_info = get_doenca_info(doenca_url)
        desc_div = div_row.find('div', class_='views-field-body')
        desc = desc_div.div.text
        doenca_info["resumo"] = desc.strip().replace(" ", " ")
        doencas[designacao] = doenca_info
    return doencas


res = {}
for a in range(ord("a"), ord("z") + 1):
    letra = chr(a)
    res = res | doencas_letra(letra)

print(res)

with open('doencas_3.json', 'w', encoding='utf-8') as f_out:
    json.dump(res, f_out, ensure_ascii=False, indent=4)
f_out.close()