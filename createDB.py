
from sqlalchemy import create_engine
import psycopg2
import psycopg2.extras
import pandas as pd

#Connection key
s = "mysql+mysqldb://max:Gentech16@192.168.4.155:3306/YuMu_db"
engine = create_engine(s)

#Create column using pandas
df = pd.DataFrame({'test':[1, 2, 3]})

#Create new test table
#df.to_sql('testable', engine, if_exists='append', index= False)


conn = engine.connect()
result = conn.execute("SELECT * FROM yumu_db.testable")
for i in result:
    print(i[0])







