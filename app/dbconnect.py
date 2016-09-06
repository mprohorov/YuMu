from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

s = "mysql+pymysql://max:Gentech16@127.0.0.1:3306/yumudb"
engine = create_engine(s)
Session = sessionmaker()

Session.configure(bind=engine)

session = Session()
conn = engine.connect()

#use  sqlalchemy to execute SQL commands
"""
conn = engine.connect()
result = conn.execute("SELECT * FROM yumu_db.account_settings")
"""