from mysql.connector import *
import sys
sys.path.insert(1, "/home/leonardo/Documents/GitHub/2022-2-BOTO")
from Boto.src.conexaoDataBase.databaseBOTO import nova_con


async def verifica_se_tem_professor_no_banco(matriculaProfessor) -> int:
    with nova_con() as con:
        try:
            SQL = "SELECT %s FROM professor WHERE matricula = %s "
            infos = (str('nome'), str(matriculaProfessor))

            cursor = con.cursor()
            cursor.execute(SQL, infos)

            busca = cursor.fetchone()

            if busca is not None:
                return True
            else:
                return False

        except ProgrammingError as e:
            print(f'Erro: {e.msg}')


async def verifica_se_senha_prof_esta_correta(senha_inserida, matricula_professor) -> int:
    with nova_con() as con:
        try:
            SQL = "SELECT senha FROM professor WHERE matricula = %s "
            infos = [(str(matricula_professor))]

            cursor = con.cursor()
            cursor.execute(SQL, infos)

            conteudo = cursor.fetchone()
            senha_correta = conteudo[0]

            if senha_correta is not None:
                if senha_correta == senha_inserida:
                    return True
                else:
                    return False
            else:
                return False

        except ProgrammingError as e:
            print(f'Erro: {e.msg}')
