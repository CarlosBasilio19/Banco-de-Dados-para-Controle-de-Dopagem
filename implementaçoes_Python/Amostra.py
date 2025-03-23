import conexao_db as db


def Listar_TodasAmostras():
    sql = "Select * from Amostras"
    db.cursor.execute(sql)
    dados_retornados = db.cursor.fetchall()
    return dados_retornados

def buscar_porID(id):
    sql = f"Select * from Amostras Where id_amostra = {id};"
    db.cursor.execute(sql)
    dados_retornados = db.cursor.fetchone()
    return dados_retornados

def busca_Numero_CodigoDaAmostra(numero):
    sql = f"Select * from Amostras where Numero_CodigoDaAmostra like '%{numero}%';"
    db.cursor.execute(sql)
    dados_retornados = db.cursor.fetchone()
    return dados_retornados

def inserir(id_amostra,Numero_CodigoDaAmostra,InicialAtleta,hora_selagem,Numero_Amostra):
    sql =f"Insert into Amostras Values('{id_amostra}', '{Numero_CodigoDaAmostra}','{InicialAtleta}','{hora_selagem}','{Numero_Amostra}',);"
    db.cursor.execute(sql)
    db.conexao.commit()


def atualizar(Numero_CodigoDaAmostra,InicialAtleta,hora_selagem,Numero_Amostra):
    sql = f"Update Amostras set Numero_CodigoDaAmostra ='{Numero_CodigoDaAmostra}',InicialAtleta ='{InicialAtleta}',hora_selagem = '{hora_selagem}',Numero_Amostra = '{Numero_Amostra}'' "
    db.cursor.execute(sql)
    db.conexao.commit()

def deletar(id):
    sql = f"DELETE FROM Amostra  WHERE id_Amostra = {id};"
    db.cursor.execute(sql)
    db.conexao.commit()