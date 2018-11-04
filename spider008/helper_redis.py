from redis import Redis

class RedisHelper():
    def __init__(self, db=3):
        self.r = Redis(
            host='127.0.0.1',
            port=6379,
            db=db,
            decode_responses=True
            )
    

    def add_redis_data(self, key, member):
        '''
        添加一条数据到指定集合
        '''
        res = self.r.sadd(key, member)
        print(res)


    def del_redis_set(self, key):
        '''
        删除指定集合中所有成员
        '''
        numbers = self.r.sdiff(key)
        count=1
        for number in numbers:
            self.r.srem(key,number)
            count +=1
        return count
    
    def get_one_data(self, key):
        '''
        获取集合中一条数据
        '''
        return self.r.spop(key)
        

    def get_num(self, key):
        '''
        统计列表数据个数
        '''
        return self.r.scard(key)


    def exist_detail_url(self, key, number):
        '''
        判断集合中的元素是否存在
        '''
        return self.r.sismember(key, number)