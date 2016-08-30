from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

s = "mysql+pymysql://max:Gentech16@68.67.148.69:3306/yumu"
engine = create_engine(s)
Session = sessionmaker()

Session.configure(bind=engine)

session = Session()
conn = engine.connect()
#s = "mysql+mysqldb://max:Gentech16@192.168.1.92:3306/yumu_db"
#engine = create_engine(s)
#Session = sessionmaker()

#Session.configure(bind=engine)

#session = Session()
#conn = engine.connect()

#use  sqlalchemy to execute SQL commands
"""
conn = engine.connect()
result = conn.execute("SELECT * FROM yumu_db.account_settings")
"""
