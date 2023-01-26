from mysql.connector import *
from Bot_teste.src.conexaoDataBase.databaseBOTO import nova_con
from telegram.ext import *

async def verifica_se_matricula_aluno_tem_no_banco(matricula) -> int:

        SQL = "SELECT %s FROM alunos WHERE matricula = %s "
        infos = (str('nome'),str(matricula))

        with nova_con() as con:
            try:
                cursor = con.cursor()
                cursor.execute(SQL, infos)

                busca = cursor.fetchone()

                if busca != None:
                    return True
                else:
                    return False

            except ProgrammingError as e :
                print(f'Erro: {e.msg}')

async def coloca_aluno_no_banco(matricula,nome)->int:

    tem_no_banco = await verifica_se_matricula_aluno_tem_no_banco(matricula)

    if tem_no_banco:
        return True
    else:
        with nova_con() as con:
            try:
                SQL2 = "INSERT INTO alunos(nome,matricula,matriculaProfessor) VALUES (%s,%s,%s)"
                infos2 = (str(nome), str(matricula), str('null'))

                cursor = con.cursor()
                cursor.execute(SQL2, infos2)
                con.commit()

                return False

            except ProgrammingError as e:
                print(f'Erro: {e.msg}')

async def verifica_se_tem_professor_no_banco(matriculaProfessor) -> int:
    SQL = "SELECT %s FROM professor WHERE matricula = %s "
    infos = (str('nome'), str(matriculaProfessor))

    with nova_con() as con:
        try:
            cursor = con.cursor()
            cursor.execute(SQL, infos)

            busca = cursor.fetchone()

            if busca != None:
                return True
            else:
                return False

        except ProgrammingError as e:
            print(f'Erro: {e.msg}')

async def cadastrando_o_professor_do_aluno(matriculaProfessor)->int:

    with nova_con() as con:
        try:
            cursor = con.cursor()

            cursor.execute("SELECT COUNT(id) FROM alunos WHERE id>0")
            numeroDeLinhas = cursor.fetchall()
            num = numeroDeLinhas[0][0]

            SQL = "UPDATE alunos SET matriculaProfessor=%s WHERE id=%s"
            val = (str(matriculaProfessor), int(num))

            cursor.execute(SQL, val)
            con.commit()

        except ProgrammingError as e:
            print(f'Erro: {e.msg}')
        else:
            print('1 id incluido, ID:', cursor.lastrowid)