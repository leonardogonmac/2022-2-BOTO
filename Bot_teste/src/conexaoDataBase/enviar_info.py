from mysql.connector import ProgrammingError
from src.conexaoDataBase.databaseBOTO import nova_con
def recebe_plano(matriculaProfessor):

    SQL = "SELECT plano_de_ensino FROM professor WHERE matricula = %s"
    parametros = [str(matriculaProfessor)]

    with nova_con() as con:
        try:
            cursor = con.cursor()
            cursor.execute(SQL, parametros)

            prof_plano = cursor.fetchone()
            professor_plano = prof_plano[0]

            print(professor_plano)

            return professor_plano

        except ProgrammingError as e:
            print(f'Erro: {e.msg}')

async def busca_professor(matriculaAluno)->int:
    SQL = "SELECT matriculaProfessor FROM alunos WHERE matricula = %s"
    param = [str(matriculaAluno)]

    with nova_con() as con:
        try:
            cursor = con.cursor()
            cursor.execute(SQL, param)

            prof_matricula = cursor.fetchone()
            prof_matricula = prof_matricula[0]

            print(prof_matricula)

            return recebe_plano(prof_matricula)

        except ProgrammingError as e:
            print(f'Erro: {e.msg}')
