import conexao_db as db

def listar_todos_testes():
    sql = "SELECT * FROM Teste"
    db.cursor.execute(sql)
    dados_retornados = db.cursor.fetchall()
    return dados_retornados

def buscar_por_id(id):
    sql = f"SELECT * FROM Teste WHERE id_teste = {id};"
    db.cursor.execute(sql)
    dados_retornados = db.cursor.fetchone()
    return dados_retornados

def buscar_por_esporte(esporte):
    sql = f"SELECT * FROM Teste WHERE esporte LIKE '%{esporte}%';"
    db.cursor.execute(sql)
    dados_retornados = db.cursor.fetchone()
    return dados_retornados

def inserir(esporte, disciplina, Cordenador_Ordem_E_Teste, Status_Competicao):
    sql = f"""
    INSERT INTO Teste (esporte, disciplina, Cordenador_Ordem_E_Teste, Status_Competiçao) 
    VALUES ('{esporte}', '{disciplina}', '{Cordenador_Ordem_E_Teste}', {Status_Competicao});
    """
    db.cursor.execute(sql)
    db.conexao.commit()

def atualizar(id_teste, esporte, disciplina, Cordenador_Ordem_E_Teste, Status_Competicao):
    sql = f"""
    UPDATE Teste 
    SET esporte = '{esporte}', disciplina = '{disciplina}', Cordenador_Ordem_E_Teste = '{Cordenador_Ordem_E_Teste}', Status_Competiçao = {Status_Competicao} 
    WHERE id_teste = {id_teste};
    """
    db.cursor.execute(sql)
    db.conexao.commit()

def deletar(id):
    sql = f"DELETE FROM Teste WHERE id_teste = {id};"
    db.cursor.execute(sql)
    db.conexao.commit()