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
import psycopg2, string, json

app = Flask(__name__)

def conectarDB():
    
    try:
        with open("./databaseConnect/bancoLivros.json", 'r') as meu_json:
            dados = json.load(meu_json)
            return (psycopg2.connect(host= dados[0]["host"], database=dados[0]["database"],user=dados[0]["user"], password=dados[0]["password"], port=dados[0]["port"]))
    except psycopg2.OperationalError as e:
        print('Unable to connect!\n{0}').format(e)      

#con = conectarDB()
#cur = con.cursor()

# 1. Consultar todos os livros cadastrados;
@app.route('/livros', methods=['GET'])
def obterLivros():
    con = conectarDB()
    cur = con.cursor()
    sql = 'select * from \"Livros\"'
    cur.execute(sql)
    livros = cur.fetchall()
    return jsonify(livros)
    cur.close()
    con.close()

# 2. Cadastrar novo livro;
@app.route('/livros', methods=['POST'])
def incluirNovoLivro():
    con = conectarDB()
    cur = con.cursor()
    novoLivro = request.get_json()
    sql = 'insert into "Livros" (id, titulo, autor) values ({}, {}, {})'.format((novoLivro["id"]), (novoLivro["titulo"]), (novoLivro["autor"]))
    cur.execute(sql)
    con.commit()
    sql = 'select * from \"Livros\"'
    cur.execute(sql)
    livros = cur.fetchall()
    return jsonify(livros)
    cur.close()
    con.close()

# 3. Consultar por id;
@app.route('/livros/<int:id>', methods=['GET'])
def obterLivroPorID(id):
    con = conectarDB()
    cur = con.cursor()
    sql = 'select * from \"Livros\"'
    cur.execute(sql)
    livros = cur.fetchall()
    for livro in livros:
        if livro[0] == id:
            return jsonify(livro)
    cur.close()
    con.close()

# 4. Editar registro por id;
@app.route('/livros/<int:id>', methods=['PUT'])
def editarLivroPorId(id):
    con = conectarDB()
    cur = con.cursor()
    livroAlterado = request.get_json()
    sql = 'update "Livros" set titulo = {}, autor = {} where id = {}'.format((livroAlterado["titulo"]), (livroAlterado["autor"]),(id))
    cur.execute(sql)
    con.commit()
    sql = 'select * from \"Livros\"'
    cur.execute(sql)
    livros = cur.fetchall()          
    return jsonify(livros)
    cur.close()
    con.close()


# 5. Excluir por id.
@app.route('/livros/<int:id>', methods=['DELETE', 'GET'])
def excluirLivroPorId(id):
    try:
        con = conectarDB()
        cur = con.cursor()
        sql = 'delete from "Livros" where id = {}'.format(id)
        cur.execute(sql)
        rows_deleted = cur.rowcount
        con.commit()

        cur.close()
    except(Exception, psycopg2.DatabaseError) as e:
        print(e)
    finally:
        if con is not None:
            con.close()
    return str(rows_deleted)
    



app.run(port=5000,host='localhost',debug=True)
#con.close()