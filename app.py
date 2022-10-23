# 1- Objetivo - Criar uma API que disponibiliza a consulta, criação, edição e exclusão de livros.
# 2- URL Base - localhost
# 3- Endpoints- 
#       - localhost/livros (GET) 
#       - localhost/livros (POST)
#       - localhost/livros/id (GET)
#       - localhost/livros/id (PUT)
#       - localhost/livros/id (DELETE)
# 4- Quais recursos - Livros

from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'titulo': 'Otelo',
        'autor': 'William Shakespeare',
    },
    {
        'id': 2,
        'titulo': 'Memorias de uma infância química',
        'autor': 'Oliver Sacks',
    },
    {
        'id': 3,
        'titulo': 'Mitologia nórdica',
        'autor': 'Neil Gaiman',
    }
]

# Com os livros criados e armazenados, devemos criar uma API com as seguintes funcionalidades:
# 1. Consultar todos;
@app.route('/livros', methods=['GET'])
def obterLivros():
    return jsonify(livros)
# 2. Incluir novo livro;
@app.route('/livros', methods=['POST'])
def incluirNovoLivro():
    novoLivro = request.get_json()
    livros.append(novoLivro)

    return jsonify(livros)
# 3. Consultar por id;
@app.route('/livros/<int:id>', methods=['GET'])
def obterLivroPorID(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)
# 4. Editar por id;
@app.route('/livros/<int:id>', methods=['PUT'])
def editarLivroPorId(id):
    livroAlterado = request.get_json()
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livroAlterado)
            return jsonify(livros[indice])
# 5. Excluir por id.
@app.route('/livros/<int:id>', methods=['DELETE'])
def excluirLivroPorId(id):
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]

    return jsonify(livros)
app.run(port=5000,host='localhost',debug=True)