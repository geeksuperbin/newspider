from redis import Redis

r = Redis(
    host='127.0.0.1',
    port=6379,
    db=4,
    decode_responses=True
)

# 向集合中添加元素
# r.sadd('cnvd:list','http://www.cnvd.org.cn/flaw/list.htm?max=100&offset=0')
# r.sadd('cnvd:list','http://www.cnvd.org.cn/flaw/list.htm?max=100&offset=100')
# r.sadd('cnvd:list','http://www.cnvd.org.cn/flaw/list.htm?max=100&offset=200')
# r.sadd('cnvd:list','http://www.cnvd.org.cn/flaw/list.htm?max=100&offset=0')

# 获取集合的成员数
print(r.scard('cnvd:list'))

# 判断元素是否在集合中
print(r.sismember('cnvd:list','http://www.cnvd.org.cn/flaw/list.htm?max=100&offset=0'))

# 移除并返回集合中的一个随机元素,没有数据会返回 None
print(r.spop('cnvd:list'))