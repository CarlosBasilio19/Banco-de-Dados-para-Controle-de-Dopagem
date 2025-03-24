import conexao_db as db

def listar_todos_enderecos():
    sql = "SELECT * FROM Endereco"
    db.cursor.execute(sql)
    dados_retornados = db.cursor.fetchall()
    return dados_retornados

def buscar_endereco_por_id(id):
    sql = f"SELECT * FROM Endereco WHERE id_endereco = {id};"
    db.cursor.execute(sql)
    dados_retornados = db.cursor.fetchone()
    return dados_retornados

def inserir_endereco(cep, numero, complemento):
    sql = f"""
    INSERT INTO Endereco (cep, numero, complemento) 
    VALUES ('{cep}', {numero}, '{complemento}');
    """
    db.cursor.execute(sql)
    db.conexao.commit()

def atualizar_endereco(id_endereco, cep, numero, complemento):
    sql = f"""
    UPDATE Endereco 
    SET cep = '{cep}', numero = {numero}, complemento = '{complemento}' 
    WHERE id_endereco = {id_endereco};
    """
    db.cursor.execute(sql)
    db.conexao.commit()

def deletar_endereco(id):
    sql = f"DELETE FROM Endereco WHERE id_endereco = {id};"
    db.cursor.execute(sql)
    db.conexao.commit()
