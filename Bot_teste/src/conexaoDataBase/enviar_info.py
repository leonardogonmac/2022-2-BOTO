from mysql.connector import ProgrammingError
from Bot_teste.src.conexaoDataBase.databaseBOTO import nova_con


def seleciona_coluna(coluna):

    if coluna == 'plano_de_ensino':
        return "SELECT plano_de_ensino FROM professor WHERE matricula = %s"
    elif coluna == 'contato':
        return "SELECT contato FROM professor WHERE matricula = %s"
def recebe_info(matriculaProfessor, coluna):
    SQL = seleciona_coluna(coluna)
    parametros = [str(matriculaProfessor)]

    with nova_con() as con:
        try:
            cursor = con.cursor()
            cursor.execute(SQL, parametros)

            prof_info = cursor.fetchone()
            info = prof_info[0]

            return info

        except ProgrammingError as e:
            print(f'Erro: {e.msg}')


async def busca_professor(matriculaAluno, coluna) -> int:
    SQL = "SELECT matriculaProfessor FROM alunos WHERE matricula = %s"
    param = [str(matriculaAluno)]

    with nova_con() as con:
        try:
            cursor = con.cursor()
            cursor.execute(SQL, param)

            prof_matricula = cursor.fetchone()
            prof_matricula = prof_matricula[0]

            return recebe_info(prof_matricula, coluna)

        except ProgrammingError as e:
            print(f'Erro: {e.msg}')
