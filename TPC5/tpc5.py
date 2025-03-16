import json
from flask import Flask, request, render_template


app = Flask(__name__)

#db_file = open("conceitos.json", encoding="utf-8")
db_file = open("conceitos_.json", encoding="utf-8")
db = json.load(db_file)
db_file.close()

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/conceitos")
def conceitos():
    designacoes = list(db.keys())
    return render_template("conceitos.html", designacoes=designacoes, title="Lista de Conceitos")

@app.route("/api/conceitos")
def api_conceitos():
    return db


@app.route("/api/conceitos/designacao")
def api_conceito(designacao):
    return {"designacao": designacao, "descricao": db[designacao]}


#-----TPC-----#
@app.route("/conceitos/<designacao>")
def o_conceito(designacao):
        if designacao in db:
            return render_template("conceito.html", designacao=designacao, descricao=db[designacao])
#-----TPC-----#


@app.post("/conceitos")
def adicionar_conceito():
    #json
    data = request.get_json()
    #{"designacao": "vida", "descricao": "a vida é..."}
    db[data["designacao"]] = data["descricao"]
    f_out = open("conceitos_.json", "w", encoding="utf") #aqui apaga completamente o que está lá por causa do w, por isso escrevemos
    #noutro ficheiro
    json.dump(db, f_out, ensure_ascii=False, indent=4)
    f_out.close()
    #form data
    return data


app.run(host="localhost", port=4002, debug=True)
