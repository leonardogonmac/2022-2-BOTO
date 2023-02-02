from mysql.connector import *
from Boto.src.conexaoDataBase.databaseBOTO import nova_con

async def buscar_professor_conteudo(matriculaAluno)->int:
    SQL = "SELECT matriculaProfessor FROM alunos WHERE matricula = %s"
    param = [str(matriculaAluno)]

    with nova_con() as con:
        try:
            cursor = con.cursor()
            cursor.execute(SQL, param)

            prof_matricula = cursor.fetchone()
            prof_matricula = prof_matricula[0]

            print(prof_matricula)

            return enviar_conteudo(prof_matricula, matriculaAluno)

        except ProgrammingError as e:
            print(f'Erro: {e.msg}')

def verifica_conteudos_enviados(matriculaAluno):

    with nova_con() as con:
        try:
            cursor = con.cursor()
            SQL_VERIFICAR_CONTEUDOS_ENVIADOS = ("SELECT COUNT(id) FROM conteudos_enviados WHERE matriculaAluno = %s")
            param_veri_cont_envi = [str(matriculaAluno)]

            cursor.execute(SQL_VERIFICAR_CONTEUDOS_ENVIADOS, param_veri_cont_envi)
            numeroDeLinhas = cursor.fetchall()
            num_conteudos_feitos = numeroDeLinhas[0][0]

            return num_conteudos_feitos

        except ProgrammingError as e:
            print(f'Erro: {e.msg}')

def conteudo_enviado(matriculaAluno,num_conteudos_feitos, prof_matricula ):
    with nova_con() as con:
        try:
            cursor = con.cursor()

            titulo_conteudo = pega_titulo_cont_feitos(num_conteudos_feitos, prof_matricula)

            SQL_ENVIADO = ("INSERT INTO conteudos_enviados(tituloConteudo,matriculaAluno) VALUES (%s, %s)")
            param_cont_enviado = (str(titulo_conteudo),str(matriculaAluno))

            cursor.execute(SQL_ENVIADO, param_cont_enviado)
            con.commit()

            print('sucesso')
        except ProgrammingError as e:
            print(f'Erro: {e.msg}')

def pega_titulo_cont_feitos(num_conteudos_feitos,prof_matricula):
    with nova_con() as con:
        try:
            cursor = con.cursor()

            SQL_CONTEUDOS_PROF = ("SELECT * FROM conteudos WHERE matriculaProfessor = %s")
            param_cont_prof = [str(prof_matricula)]

            cursor.execute(SQL_CONTEUDOS_PROF, param_cont_prof)
            conteudos = cursor.fetchall()

            titulo = conteudos[num_conteudos_feitos][1]

            return titulo

        except ProgrammingError as e:
            print(f'Erro: {e.msg}')

def verifica_numero_de_conteudos(prof_matricula):
    with nova_con() as con:
        try:
            cursor = con.cursor()
            SQL = ("SELECT COUNT(id) FROM conteudos WHERE matriculaProfessor = %s")
            param= [str(prof_matricula)]

            cursor.execute(SQL, param)
            numeroDeLinhas = cursor.fetchall()
            num_conteudos = numeroDeLinhas[0][0]

            return num_conteudos

        except ProgrammingError as e:
            print(f'Erro: {e.msg}')

def enviar_conteudo(prof_matricula, matriculaAluno) :

        with nova_con() as con:
            try:
                cursor = con.cursor()

                num_conteudos_feitos = verifica_conteudos_enviados(matriculaAluno)

                SQL_CONTEUDO_PARA_ENVIAR = ("SELECT * FROM conteudos WHERE matriculaProfessor = %s")
                param_cont_p_enviar = [str(prof_matricula)]

                cursor.execute(SQL_CONTEUDO_PARA_ENVIAR, param_cont_p_enviar)
                conteudos = cursor.fetchall()

                num_conteudos = verifica_numero_de_conteudos(prof_matricula)

                if (num_conteudos_feitos == num_conteudos ):
                    return False
                else:
                    print(conteudos[num_conteudos_feitos])

                    conteudo_a_ser_enviado = conteudos[num_conteudos_feitos]

                    conteudo_enviado(matriculaAluno, num_conteudos_feitos,prof_matricula)

                    return conteudo_a_ser_enviado

            except ProgrammingError as e :
                print(f'Erro: {e.msg}')
