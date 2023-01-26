from mysql.connector import connect
from contextlib import contextmanager

parametros = dict(
    host='35.247.224.118',
    port=3306,
    user='root',
    password='Eda{]OAlb(}1I:`k',
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