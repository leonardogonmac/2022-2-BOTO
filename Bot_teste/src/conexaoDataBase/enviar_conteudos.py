from mysql.connector import ProgrammingError
import pandas as pd
from src.conexaoDataBase.databaseBOTO import nova_con
async def enviar_planilha_banco() ->int:

    tabela = pd.read_excel("./conexaoDataBase/PlanilhasPreenchidas/planilha_preenchida.xlsx")
    numeroDeLinhas = len(tabela.index)
    print(numeroDeLinhas)

    for i in range(numeroDeLinhas):
        titulo = tabela['titulo'] [i]
        link = tabela['link'] [i]
        link_extra = tabela['link_extra'] [i]
        matriculaProfessor = 123456

        SQL = "INSERT INTO conteudos(titulo, link, link_extra,matriculaProfessor) VALUES (%s,%s,%s,%s)"
        conteudos= (str(titulo),str(link),str(link_extra),str(matriculaProfessor))

        with nova_con() as con:
            try:
                cursor = con.cursor()
                cursor.execute(SQL, conteudos)
                con.commit()
                print("sucesso")
            except ProgrammingError as e :
                print(f'Erro: {e.msg}')
            else:
                print('1 id incluido, ID:',cursor.lastrowid)
