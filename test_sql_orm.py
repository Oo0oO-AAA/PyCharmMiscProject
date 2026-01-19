from    sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.orm import declarative_base, sessionmaker

#创建数据引擎库
engin = create_engine('mysql+pymysql://root:123456@localhost:3306/test2')
charset = 'utf8'
Base = declarative_base()
Session = sessionmaker(bind=engin)
session = Session()
class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True,autoincrement=True)
    name = Column(String(20),nullable=False)
    gender = Column(String(20),nullable=False)
    age = Column(Integer,nullable=False)
#查询年龄>25的学生
filter_students = session.query(Student).filter(Student.age>=25).all()
for i in filter_students:
    print(i.name,i.gender,i.age)
session.close()



