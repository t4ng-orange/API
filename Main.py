from flask import Flask , request, jsonify

app = Flask(__name__)
#informações

jogos = [
    {
    'id':1,
    'titulo': 'pacman',
    'criador': 'Toru Iwatani'
    },
    {'id': 2,
     'titulo':'megaman',
      'criador': 'capcom' 
    },
    {'id': 3,
     'titulo': 'minecraft', 
    'criador': 'notch'
    }
]
#consultar todos
@app.route('/jogos',methods = ['GET'])
def obter_jogos():
    return jsonify(jogos)

#consultar id
@app.route('/jogos/<int:id>',methods = ['GET'])
def obter_jogo_por_id(id):
    for jogo in jogos:
        if jogo.get('id') == id:
            return jsonify(jogo)
        
#editar         
@app.route('/jogos/<int:id>',methods = ['PUT'])
def editar_jogo_por_id(id):
    jogo_alterado = request.get_json()
    for indice in enumerate (jogos):
        if jogos.get('id') == id:
            jogos[indice].update(jogo_alterado)
            return jsonify(jogos[indice])

#cria um novo jogo  (adiciona um novo jogo na lista do dicionário)
@app.route('/jogos/',methods = ['POST'] )
def criar_novo_jogo():
    novo_jogo = request.get_json()
    jogos.append(novo_jogo)
    return jsonify(jogos)

#excluir (exclui um jogo especifico da lista)
@app.route('/jogos/<int:id>',methods = ['DELETE'])
def deletar_jogo(id):
    for indice, jogo in enumerate(jogos):
        if jogo.get('id') == id:
            del jogos[indice]
#rodar api
app.run(port = 5000, host = 'localhost', debug = False)

