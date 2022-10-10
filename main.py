from logging import exception
from multiprocessing import connection
from subprocess import SubprocessError
import pymysql
from train_PyMySQL.config import host, user, password, db_name


try: 
    connection = pymysql.connect(
    host=host,
    user =user,
    port= 3306,
    password= password,
    database= db_name,
    cursorclass=  pymysql.cursors.DictCursor
    )
    print(" successfully connected...")
except exception as ex:
    print("Connection refused...")
    print(ex)