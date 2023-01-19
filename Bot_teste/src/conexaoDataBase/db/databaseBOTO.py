from mysql.connector import connect
from contextlib import contextmanager

parametros = dict(
    host='localhost',
    port=3306,
    user='username',     ## usar nome do seu usuario
    password='Beavn/02', ## usar senha do seu DB
    database='BOT'
)
@contextmanager
def nova_con():
    con = connect(**parametros)
    try:
        yield con
    finally:
        if(con and con.is_connected()):
            con.close()