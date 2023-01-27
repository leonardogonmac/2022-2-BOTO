from mysql.connector import *
from src.conexaoDataBase.databaseBOTO import nova_con
import pandas as pd
#async def pega_titulo_atual() -> str:


async def busca_professor_conteudo(matriculaAluno)->int:
    SQL = "SELECT matriculaProfessor FROM alunos WHERE matricula = %s"
    param = [str(matriculaAluno)]

    with nova_con() as con:
        try:
            cursor = con.cursor()
            cursor.execute(SQL, param)

            prof_matricula = cursor.fetchone()
            prof_matricula = prof_matricula[0]

            print(prof_matricula)

            return recebe_conteudo(prof_matricula, matriculaAluno)

        except ProgrammingError as e:
            print(f'Erro: {e.msg}')

def recebe_conteudo(prof_matricula, matriculaAluno) :


        with nova_con() as con:
            try:
                cursor = con.cursor()

                SQL = ("SELECT COUNT(id) FROM conteudos_feitos WHERE matriculaAluno = %s")
                param = [str(matriculaAluno)]

                cursor.execute(SQL,param)
                numeroDeLinhas = cursor.fetchall()
                num_conteudos_feitos = numeroDeLinhas[0][0]

                SQL2 = ("SELECT * FROM conteudos WHERE matriculaProfessor = %s")
                param2 = [str(prof_matricula)]

                cursor.execute(SQL2, param2)
                conteudos = cursor.fetchall()

                print(conteudos[num_conteudos_feitos])

                #cursor.execute(SQL)
                #row = cursor.fetchone()
                #print(row)

                print("sucesso")
            except ProgrammingError as e :
                print(f'Erro: {e.msg}')

recebe_conteudo(123456,123456789)