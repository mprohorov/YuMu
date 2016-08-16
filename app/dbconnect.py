from sqlalchemy import create_engine

s = "mysql+mysqldb://max:Gentech16@192.168.0.11:3306/yumu_db"
engine = create_engine(s)

conn = engine.connect()

#use  sqlalchemy to execute SQL commands
"""
conn = engine.connect()
result = conn.execute("SELECT * FROM yumu_db.account_settings")
"""