"""
    terminal操作
    db ----查看当前数据库
    use xxx;  ---使用，没有就创建xxx
    stu = {'a':'a'}
    db.xxx.insert(stu)
    db.xxx.find()
    db.xxx.findOne()
    修改
    p = db.xxx.findOne()
    p.name = 'john'
    db.xxx.update({name:'jhon'}, p)
    db.xxx.remove({name:'john'})
    db.xxx.remove({})  ------- 清空数据库

    db.xxx.find({name:'jhon'}, {name:true,id:false})
"""
from datetime import datetime

import pymongo
from bson.objectid import ObjectId


# client = pymongo.MongoClient()
# client = pymongo.MongoClient('mongodb://localhost:27017/')
# client = pymongo.MongoClient('localhost', 27017) #mongodb 默认携带线程池，不用client.close()

class TestMongo(object):

    def __init__(self):
        self.client = pymongo.MongoClient()
        self.db = self.client['emr']
        self.collection = self.db['test']

    def add_one(self):
        post = {
            'title': '标题',
            'content': '内容',
            'insertTime': datetime.now()
        }
        return self.collection.insert_one(post)

    def get_one(self):
        return self.collection.find_one()

    def get_more(self):
        return self.collection.find()

    def get_one_from_oid(self, oid):
        """
        查询指定ID的数据
        :param oid:
        :return:
        """
        obj = ObjectId(oid)
        return self.collection.find_one({'_id': obj})

    def update(self):
        self.collection.update_one({'title': '标题'}, {'$set': {'content': '修改了'}})
        self.collection.update_many({'title': '标题'}, {'$set': {'content': '修改了1'}})

    def delete(self):
        self.collection.delete_one({'title': '标题'})
        self.collection.delete_one({'title': '标题'})


def main():
    obj = TestMongo()
    rest = obj.add_one()
    # print(rest)
    print(obj.get_one())
    print([i for i in obj.get_more()])
    print(obj.get_one_from_oid('5fdd722fde7ef284eae6dbaf'))
    obj.update()
    print([i for i in obj.get_more()])
    obj.delete()
    print([i for i in obj.get_more()])


if __name__ == '__main__':
    main()
