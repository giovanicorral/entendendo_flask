#Vamos criar um dicionário com duas chaves e tentar retornar seus dados pela rota
dicionario = {
    "nome" : "André David",
    "nascimento":1989
}

#importar flask
from flask import Flask
#Criar a aplicação Flask
app = Flask(__name__)

#A rota abaixo aciona uma função que retorna um dicionário
@app.route("/teste")
def mostra_dicionario():
    return dicionario

@app.route("/")
def dados_usuario():
    return f"<b>O usuário {dicionario['nome']} nasceu em {dicionario['nascimento']}<b>"

#Colocar a aplicação para rodar
app.run(debug=True)