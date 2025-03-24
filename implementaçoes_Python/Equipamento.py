import conexao_db as db

def listar_todos_equipamentos():
    sql = "SELECT * FROM Equipamento"
    db.cursor.execute(sql)
    dados_retornados = db.cursor.fetchall()
    return dados_retornados

def buscar_equipamento_por_id(id):
    sql = f"SELECT * FROM Equipamento WHERE id_Equipamento = {id};"
    db.cursor.execute(sql)
    dados_retornados = db.cursor.fetchone()
    return dados_retornados

def inserir_equipamento(fabricante, modelo):
    sql = f"""
    INSERT INTO Equipamento (fabricante, modelo) 
    VALUES ('{fabricante}', '{modelo}');
    """
    db.cursor.execute(sql)
    db.conexao.commit()

def atualizar_equipamento(id_Equipamento, fabricante, modelo):
    sql = f"""
    UPDATE Equipamento 
    SET fabricante = '{fabricante}', modelo = '{modelo}' 
    WHERE id_Equipamento = {id_Equipamento};
    """
    db.cursor.execute(sql)
    db.conexao.commit()

def deletar_equipamento(id):
    sql = f"DELETE FROM Equipamento WHERE id_Equipamento = {id};"
    db.cursor.execute(sql)
    db.conexao.commit()