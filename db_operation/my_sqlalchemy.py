from sqlalchemy import create_engine, Column, Integer, String, DateTime, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

engine = create_engine('mysql+pymysql://root:weiqi19960906@localhost:3306/mysqltest')
# engine = create_engine('mysql+pymysql://root:weiqi19960906@localhost:3306/mysqltest?charset=utf8')
Base = declarative_base()
Session = sessionmaker(bind=engine)


class News(Base):
    __tablename__ = 'news'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(200), nullable=False)
    time = Column(DateTime, default=datetime.datetime.now)


class OrmTest(object):
    def __init__(self):
        self.session = Session()

    def add_one(self):
        new_obj = News(title="测试")
        new_obj1 = News(title="测试2")
        # self.session.add(new_obj)
        # self.session.add(new_obj1)
        self.session.add_all([new_obj, new_obj1])
        self.session.commit()

    def get_one(self):
        return self.session.query(News).get(2)

    def get_more(self):
        # order_by
        return self.session.query(News).filter(News.id > 1).all()

    def update_one(self):
        obj = self.session.query(News).filter(News.id > 1).first()
        obj.title = '修改测试'
        self.session.commit()

    def delete_one(self):
        obj = self.session.query(News).filter(News.id > 1).first()
        self.session.delete(obj)
        self.session.commit()


if __name__ == '__main__':
    if 'news' in engine.table_names():
        table = Table("news", Base.metadata, autoload=True)
        table.drop(engine)
    News.metadata.create_all(engine)
    o = OrmTest()
    o.add_one()
    print(o.get_one().title)
    print(o.get_more()[0].title)
    o.update_one()
    print(o.get_more()[0].title)
    o.delete_one()
    if not o.get_more():
        print("删除成功")
