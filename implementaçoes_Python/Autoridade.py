from os import system
system('cls')
import conexao_db as db


def listar_todas_autoridades():
    sql = "SELECT * FROM Autoridade"
    db.cursor.execute(sql)
    dados_retornados = db.cursor.fetchall()
    return dados_retornados

def buscar_autoridade_por_id(id):
    sql = f"SELECT * FROM Autoridade WHERE id_autoridade = {id};"
    db.cursor.execute(sql)
    dados_retornados = db.cursor.fetchone()
    return dados_retornados

def inserir_autoridade(AutoridadeDeTeste, AutoridadeDeColeta, AutoridadeDeGestao, CoordenadorDeControleDopagem):
    sql = f"""
    INSERT INTO Autoridade (AutoridadeDeTeste, AutoridadeDeColeta, AutoridadeDeGestao, CoordenadorDeControleDopagem) 
    VALUES ('{AutoridadeDeTeste}', '{AutoridadeDeColeta}', '{AutoridadeDeGestao}', '{CoordenadorDeControleDopagem}');
    """
    db.cursor.execute(sql)
    db.conexao.commit()

def atualizar_autoridade(id_autoridade, AutoridadeDeTeste, AutoridadeDeColeta, AutoridadeDeGestao, CoordenadorDeControleDopagem):
    sql = f"""
    UPDATE Autoridade 
    SET AutoridadeDeTeste = '{AutoridadeDeTeste}', 
        AutoridadeDeColeta = '{AutoridadeDeColeta}', 
        AutoridadeDeGestao = '{AutoridadeDeGestao}', 
        CoordenadorDeControleDopagem = '{CoordenadorDeControleDopagem}' 
    WHERE id_autoridade = {id_autoridade};
    """
    db.cursor.execute(sql)
    db.conexao.commit()

def deletar_autoridade(id):
    sql = f"DELETE FROM Autoridade WHERE id_autoridade = {id};"
    db.cursor.execute(sql)
    db.conexao.commit()
