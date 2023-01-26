from mysql.connector import *
from Bot_teste.src.conexaoDataBase.databaseBOTO import nova_con
import pandas as pd
#async def pega_titulo_atual() -> str:

async def enviar_planilha_banco() ->int:

        SQL = "SELECT * FROM conteudos WHERE titulo = "

        with nova_con() as con:
            try:
                cursor = con.cursor()
                cursor.execute(SQL)
                row = cursor.fetchone()
                print(row)

                print("sucesso")
            except ProgrammingError as e :
                print(f'Erro: {e.msg}')
            else:
                print('1 id incluido, ID:',cursor.lastrowid)

