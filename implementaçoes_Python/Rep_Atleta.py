import conexao_db as db

def listar_todos_rep_atletas():
    sql = "SELECT * FROM Rep_Atleta"
    db.cursor.execute(sql)
    dados_retornados = db.cursor.fetchall()
    return dados_retornados

def buscar_rep_atleta_por_id(id):
    sql = f"SELECT * FROM Rep_Atleta WHERE id_Rep_Atleta = {id};"
    db.cursor.execute(sql)
    dados_retornados = db.cursor.fetchone()
    return dados_retornados

def inserir_rep_atleta(nome, sobrenome):
    sql = f"""
    INSERT INTO Rep_Atleta (nome, sobrenome) 
    VALUES ('{nome}', '{sobrenome}');
    """
    db.cursor.execute(sql)
    db.conexao.commit()

def atualizar_rep_atleta(id_Rep_Atleta, nome, sobrenome):
    sql = f"""
    UPDATE Rep_Atleta 
    SET nome = '{nome}', sobrenome = '{sobrenome}' 
    WHERE id_Rep_Atleta = {id_Rep_Atleta};
    """
    db.cursor.execute(sql)
    db.conexao.commit()

def deletar_rep_atleta(id):
    sql = f"DELETE FROM Rep_Atleta WHERE id_Rep_Atleta = {id};"
    db.cursor.execute(sql)
    db.conexao.commit()
