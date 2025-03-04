import mysql.connector
import sys
import os 
from dotenv import load_dotenv
from pathlib import Path

def loadenv():
    script_dir = Path(__file__).parent.resolve()
    load_dotenv(script_dir / '.env')
    mydb = mysql.connector.connect(
      host=os.getenv('MYSQL_HOST'),
      user=os.getenv('MYSQL_USER'),
      password=os.getenv('MYSQL_PASSWORD'),
      database=os.getenv('MYSQL_DATABASE')
    )
    return mydb
def checkenv():
    script_dir = Path(__file__).parent.resolve()
    load_dotenv(script_dir / '.env')
    print(os.getenv('MYSQL_HOST'))
    print(os.getenv('MYSQL_USER'))
    print(os.getenv('MYSQL_PASSWORD'))
    print(os.getenv('MYSQL_DATABASE'))
def conection(query):
    mydb = loadenv()
    mydbcursor = mydb.cursor()
    mydbcursor.execute(query)
    myresult = mydbcursor.fetchall()
    for x in myresult:
      print(x)
    mydbcursor.close()
    mydb.close()
    
def insert(insert):
    mydb = loadenv()
    mydbcursor = mydb.cursor()
    for x in insert:
      mydbcursor.execute("INSERT INTO sensordata (calle, valor) VALUES (%s, %s)", (x['calle'], x['valor']))
    mydb.commit()
    mydbcursor.close()
    mydb.close()
    