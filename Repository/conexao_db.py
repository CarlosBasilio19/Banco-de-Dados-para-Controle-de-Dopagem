import mysql.connector

conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="6363",
        database="Sistema_de_Controle_de_Dopagem"
    )


cursor = conexao.cursor()

print("✅ Conectado ao banco de dados")





