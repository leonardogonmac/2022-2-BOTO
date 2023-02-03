from mysql.connector import ProgrammingError
from Boto.src.conexaoDataBase.databaseBOTO import nova_con
import pandas as pd


async def enviar_planilha_banco(matricula_professor) -> int:
    tabela = pd.read_excel(f"./conexaoDataBase/PlanilhasPreenchidas/{matricula_professor}.xlsx")
    numeroDeLinhas = len(tabela.index)
    print(numeroDeLinhas)

    for i in range(numeroDeLinhas):
        titulo = tabela['titulo'][i]
        link = tabela['link'][i]
        link_extra = tabela['link_extra'][i]
        matriculaProfessor = matricula_professor

        SQL = "INSERT INTO conteudos(titulo, link, link_extra,matriculaProfessor) VALUES (%s,%s,%s,%s)"
        conteudos = (str(titulo), str(link), str(link_extra), str(matriculaProfessor))

        with nova_con() as con:
            try:
                cursor = con.cursor()
                cursor.execute(SQL, conteudos)
                con.commit()
            except ProgrammingError as e:
                print(f'Erro: {e.msg}')

