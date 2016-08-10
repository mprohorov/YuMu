
from sqlalchemy import create_engine
import psycopg2
import psycopg2.extras
import pandas as pd

#Connection key
s = "mysql+mysqldb://max:Gentech16@192.168.4.155:3306/YuMu_db"
engine = create_engine(s)

# df = pd.DataFrame({'test':[1, 2, 3]})- Example DataFrame construction

#Create new test table

account_settings = pd.DataFrame()
account_settings.to_sql('account_settings', engine, if_exists='append', index= False)


conn = engine.connect()
result = conn.execute("SELECT * FROM yumu_db.account_settings")
for i in result:
    print(i[0])







