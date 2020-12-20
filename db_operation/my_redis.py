"""
    redis:  速度快，保存到内存当中
    用途 数据库、缓存、消息中间件
    类型 字符串、散列、列表、集合、有序集合

    redis-server    开启redis
    redis-cli       进入redis
    shutdown        关闭redis
    set key value   设置值
    get key         获得值
    mset key1 value1 key2 value2 key3 value3    多key设置
    mget key1 key2 key3                         多key获得
    append key value    追加value
    del key         删除值
    incr/decr       增加1/减少1
    set key value EX 5  设置值后5秒钟自动删除

    redis------list

    lpush   左新增
    llen    长度
    rpush   右新增
    lrange  拿一段数据   lrange q1 0 -1   拿所有元素
    ltrim   截取一段数据，原list被截断
    lpushx/rpushx   key存在可增，不存在不可增
    lpop/rpop   推出元素

    redis------set
    sadd/srem   添加/删除元素
    sismember   判断是否为set的一个元素
    smembers    返回该集合的所有成员
    sdiff       返回一个集合与其他集合的差异
    sinter      返回几个集合的交集
    sunion      返回几个集合的并集

    redis------Hash 散列
    hset/hget   设置/获取散列值    hset news:1 title "news title"
    hmset/hmget 设置/获取多对散列值  hmget news:1 title content
    hsetnx      如果散列已经存在，则不设置
    hkeys/hvals 返回所有keys/values
    hlen        返回散列包含域field的数量
    hdel        删除散列指定的域
    hexists     判断是否存在
"""

"""
    python 操作redis
    pip install redis
"""
import redis


# r = redis.StrictRedis(host='localhost', port=6379, db=0)
# r = redis.Redis(host='localhost', port=6379, db=0)   --- 兼容老版本封装
# r.set('user1', '1')
# user1 = r.get('user1')
# print(user1)

class TestString(object):

    def __init__(self):
        self.r = redis.StrictRedis(host='localhost', port=6379, db=0)

    def test_string(self):
        """
            set
            get
            mset    设置多个
            mget    获取多个
            delete
        """
        self.r.set('user2', 'Amy')
        print(self.r.get('user2'))
        self.r.mset({
            'user3': 'A',
            'user4': 'B'
        })
        print(self.r.mget(['user3', 'user4']))
        self.r.delete('user3')
        print(self.r.get('user3'))
        self.r.append('user4', 'BB')
        print(self.r.get('user4'))

    def test_list(self):
        """
        lpush   左新增
        llen    长度
        rpush   右新增
        lrange  拿一段数据   lrange q1 0 -1   拿所有元素
        ltrim   截取一段数据，原list被截断
        lpushx/rpushx   key存在可增，不存在不可增(list 存在可增，不存在不可增)
        lpop/rpop   推出元素
        """
        self.r.lpush('l1', 'a')
        print(self.r.lrange('l1', 0, -1))
        self.r.lpushx('l1', 'a')
        self.r.lpushx('l1', 'b')
        print(self.r.lrange('l1', 0, -1))
        for i in range(4):
            self.r.rpop('l1')
        print(self.r.lrange('l1', 0, -1))

    def test_set(self):
        """
        redis------set
        sadd/srem   添加/删除元素
        sismember   判断是否为set的一个元素
        smembers    返回该集合的所有成员
        sdiff       返回一个集合与其他集合的差异
        sinter      返回几个集合的交集
        sunion      返回几个集合的并集
        """
        self.r.sadd('s1', 'a')
        print(self.r.sismember('s1', 'a'))
        print(self.r.sismember('s1', 'b'))
        print(self.r.smembers('s1'))


def main():
    ts = TestString()
    # ts.test_string()
    # ts.test_list()
    ts.test_set()


if __name__ == '__main__':
    main()
