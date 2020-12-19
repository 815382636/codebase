"""
    Object Document Mapping
    mongoengine
    flask-mongoengine
"""
from mongoengine import connect, DynamicDocument, EmbeddedDocument, Document, StringField, IntField, FloatField, \
    ListField, \
    EmbeddedDocumentField

"""
    几种连接方式
"""
db = connect('emr')
db = connect('emr', host='localhost', port=27017)
db = connect('emr', host='localhost', port=27017, username='xxx', password='xxx')
db = connect('emr', host='mongodb://localhost/emr')

"""
StringField,
ObjectIdField,
IntField,
FloatField,
DecimalField,
BooleanField,
DateTimeField,
ListField
"""


class Grade(EmbeddedDocument):
    ''' 成绩 '''
    name = StringField(required=True)
    score = FloatField(required=True)


SEX_CHOICES = (
    ('male', '男'),
    ('female', '女')
)


# class Student(Document):
class Student(DynamicDocument):   # 可以另外添加字段
    name = StringField(max_length=32, required=True)
    age = IntField(required=True)
    grade = FloatField()
    address = StringField()
    sex = StringField(choices=SEX_CHOICES, required=True)
    grades = ListField(EmbeddedDocumentField(Grade))

    meta = {
        'collection': 'student'
    }


class TestMongoEngine:
    def __init__(self):
        self.db = connect('emr', host='localhost', port=27017)

    def add_one(self):
        yuwen = Grade(
            name='yuwen',
            score=75
        )
        shuxue = Grade(
            name='shuxue',
            score=80
        )
        stu_obj = Student(
            name='张三1',
            age=15,
            sex='male',
            grades=[shuxue, yuwen]
        )
        stu_obj.save()
        return stu_obj

    def get_one(self):
        return Student.objects.first()

    def get_more(self):
        return Student.objects.all()

    def get_from_id(self, oid):
        return Student.objects.filter(pk=oid).first()

    def update(self):
        #   修改一条数据
        return Student.objects.filter(name='张三').update_one(set__age=20)
        #   修改多条数据
        # return Student.objects.filter(name='张三').update(set__age=20)

    def delete(self):
        # 删除一条数据
        return Student.objects.filter(name='张三1').first().delete()
        # 删除多条数据
        # return Student.objects.filter(name='张三1').delete()


def main():
    obj = TestMongoEngine()
    rest = obj.add_one()
    print(rest.id)
    print(obj.get_one().name)
    print([i.name for i in obj.get_more()])
    print(obj.get_from_id('5fddac2941f3b04decc345a9').name)
    # print(obj.update())
    # print(obj.delete())


if __name__ == '__main__':
    main()
