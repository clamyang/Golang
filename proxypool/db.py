# Redis数据库地址
REDIS_HOST = '127.0.0.1'

# Redis端口
REDIS_PORT = 6379

# Redis密码，如无填None
REDIS_PASSWORD = 'foobared'

REDIS_KEY = 'proxies'

# 代理分数
MAX_SCORE = 100
MIN_SCORE = 0
INITIAL_SCORE = 10

import redis
from random import choice

class RedisClient(object):
    def __init__(self, host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD):
        """
        初始化
        :param host: Redis 地址
        :param port: Redis 端口
        :param password: Redis 密码

        """
        self.db = redis.StrictRedis(host=host, port=port, password=password, decode_responses=True)
        #print('连接成功')

    def add(self,proxy, score=INITIAL_SCORE):
        """
        添加代理，设置分数为最高
        :param proxy: 代理
        :param score: 分数
        :return: 添加的结果
        """
        if not self.db.zscore(REDIS_KEY, proxy):
            self.db.zadd(REDIS_KEY, score, proxy)

    def random(self):
        """
        随机获取有效代理， 首先尝试获取最高分数代理，如果最高分数不存在，则按照排名获取，否则异常。
        :return: 随机代理
        """

        result = self.zrangebyscore(REDIS_KEY, MAX_SCORE, MAX_SCORE)
        if len(result):
            return choice(result)
        else:
            result = self.zrangebyscore(REDIS_KEY, 0, 100)
            if len(result):
                return choice(result)
            else:
                raise ProxypoolEmpty

    def decrease(self, proxy):
        """
        代理值减一分，如果分数小于最小值，则代理删除。
        :param proxy: 代理
        :return: 修改后的代理分数
        """
        #返回有序集 key 中，成员 member 的 score 值。如果 member 元素不是有序集 key 的成员，或 key 不存在，返回 nil 。
        score = self.db.zscore(REDIS_KEY, proxy)
        if score and score > MIN_SCORE:
            print('代理', proxy, '当前分数', score, '减 1 ')
            return self.db.zincrby(REDIS_KEY, proxy, -1)
        else:
            print('代理', proxy, '当前分数', score, '移除')
            return self.db.zrem(REDIS_KEY, proxy)

    def exist(self, proxy):
        """
        判断代理是否存在
        :return: 是否存在
        """

        return not self.db.zscore(REDIS_KEY, proxy) == None

    def max(self, proxy):
        """
        将代理设置为MAX_SCORE
        :param proxy: 代理
        :return: 设置结果
        """

        print('代理', proxy, '可用，设置分数为', MAX_SCORE)
        return self.db.zadd(REDIS_KEY, MAX_SCORE, proxy)

    def count(self):
        """
        获取数量
        :return: 数量
        """

        return self.db.zcard(REDIS_KEY)

    def all(self):
        """
        获取全部代理
        """
        return self.zrangebyscore(REDIS_KEY, MIN_SCORE, MAX_SCORE)

redis = RedisClient()
result = redis.add('127.0.0.1')
print(result)

redis.max('127.0.0.1')


