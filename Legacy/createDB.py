
from sqlalchemy import create_engine
import psycopg2
import psycopg2.extras
import pandas as pd
import numpy as np;

#Connection key
s = "mysql+mysqldb://max:Gentech16@148.4.117.98:3306/yumu_db"
engine = create_engine(s)

# df = pd.DataFrame({'test':[1, 2, 3]})- Example DataFrame construction


conn = engine.connect()
result = conn.execute("SELECT * FROM yumu_db.account_settings")
for i in result:
    print(i)
print(account_settings.dtypes)







