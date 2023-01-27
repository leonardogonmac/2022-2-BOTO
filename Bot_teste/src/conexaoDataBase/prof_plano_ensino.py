from mysql.connector import ProgrammingError
from src.conexaoDataBase.databaseBOTO import nova_con

"""Função que recebe o link do plano de ensino e a coloca na tabela do banco de dados"""
async def colocar_plano(link) -> int:

    SQL = "UPDATE professor SET plano_de_ensino = %s WHERE matricula= %s "
    val = (str(link), "123456")

    with nova_con() as con:
        try:
            cursor = con.cursor()
            cursor.execute(SQL,val)
            con.commit()
            print("sucesso")
        except ProgrammingError as e:
            print(f'Erro: {e.msg}')
        else:
            print('1 id incluido, ID:', cursor.lastrowid)
