import conexao_db as db

def listar_todos():
    sql = "SELECT * FROM Atleta;"
    db.cursor.execute(sql)
    dados_retornados = db.cursor.fetchall()
    return dados_retornados

def buscar_por_id(id):
    sql = f"SELECT * FROM Atleta WHERE id_Atleta  = {id};"
    db.cursor.execute(sql)
    dados_retornados = db.cursor.fetchone()
    return dados_retornados

def buscar_por_nome(nome):
    sql = f"SELECT * FROM Atleta  WHERE nome LIKE '%{nome}%';"
    db.cursor.execute(sql)
    dados_retornados = db.cursor.fetchall()
    return dados_retornados

def inserir(nome,data_nascimento):
    sql = f"INSERT INTO Atleta  (nome, dataNascimento) VALUES('{nome}','{data_nascimento}');"
    db.cursor.execute(sql)
    db.conexao.commit()

def atualizar(id, nome, data_nascimento):
    sql = "UPDATE Atleta  SET nome = %s, dataNascimento = %s WHERE id_Atleta = %s;"
    sql = f"UPDATE Atleta  SET nome = {nome}, dataNascimento = %s WHERE id_Atleta = %s;"
    db.cursor.execute(sql, (nome, data_nascimento, id))
    db.conexao.commit()

def deletar(id):
    sql = f"DELETE FROM Atleta  WHERE id_Atleta = {id};"
    db.cursor.execute(sql)
    db.conexao.commit()

deletar(13)

