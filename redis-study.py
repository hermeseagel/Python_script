# -*- coding: utf-8 -*-
import redis
redis = redis.Redis(host='192.168.0.200',port=6379,password='G1obalH@wk')

#redis.lpush('listexample','aa')#在左方塞入值
#redis.lpush('listexample','cc')
#redis.rpush('listexample','JJ')#在右方塞入值
#print(redis.llen('listexample'))
#print(redis.lrange('listexample',0,8)) #一律從位置0算起
'''9
['cc', 'aa', 'cc', 'aa', 'cc', 'aa', 'JJ', 'JJ', 'JJ']'''
#print(redis.rpush('listexample',99))
#print(redis.lrange('listexample',0,9))
"""會在右邊加入值，或加入多個值
['cc', 'aa', 'cc', 'aa', 'cc', 'aa', 'JJ', 'JJ', 'JJ', '99']
""" 
#print(redis.lpop('listexample'))
'''cc 被移掉'''
#print(redis.lrange('listexample',0,-1))
'''['aa', 'cc', 'aa', 'JJ', 'JJ', 'JJ', '99', '99']'''
#print(redis.rpop('listexample')) #從list右方取出值且移除
#print(redis.lrange('listexample',0,-1))
'''99
['aa', 'cc', 'aa', 'JJ', 'JJ', 'JJ', '99']
'''
#在"99" 之前插入"XX"
#print(redis.linsert('listexample',"before","99","XX"))
#print(redis.lrange('listexample',0,-1))
'''['aa', 'cc', 'aa', 'JJ', 'JJ', 'JJ', 'XX', '99']''' 
#print(help(redis.lset))
print(redis.lset('listexample',2,'Victory')) ＃設定在那個INDEX位置 更新值
print(redis.lrange('listexample',0,-1))
'''
True
['jjj', 'cc', 'Victory', 'JJ', 'JJ', 'JJ', 'XX', '99']
'''
#print(help(redis.linsert))
#以下是針對HASMAP 的範例
#將Dict 丟入 Redis 會被當String  來處理
#lists={'a':1,'b':'cc','c':4455}
#redis.hset('lista','nomean',lists)
#ll=redis.hget('lista','nomean')
#print(ll)
'''輸出的結果：{'a': 1, 'c': 4455, 'b': 'cc'}'''

#而可以用 redis.hset 的方式將 Key name  放入一個 hset 中, 再取出就是 DICT
#如果你需要一組主KEY 對映多個值，可以用hmset 來處理
redis.hmset('testss',{'aa':'bb','cc':'dd'})
#print(redis.hmget('testss','cc'))
###
'''輸出結果為：['dd']'''

redis.hset('listsc','a',1)
redis.hset('listsc','b',2)
#print(redis.hget('listsc'))
#去判斷是否存在列表中, Return exists Trun , False
#print(redis.hexists('listsc','a'))
#使用hkeys 將特定Hash 中的KEY列出
#print(redis.hkeys('listsc'))
#l2=redis.hgetall('listsc')
#print(l2)
#print(type(l2))
#for example hincrby , 出來的結果為無序的
#redis.hset('modelclick','D0001',1)
#redis.hset('modelclick','D0002',1)
#redis.hset('modelclick','D0003',1)
#redis.hincrby('modelclick','D0003',1)
#print(redis.hgetall('modelclick'))
#sorted sets 
#zadd 是有序的，而zadd(序列名稱,序列成員,分數）
#redis.zadd('modelrank','D0001',1)
#redis.zadd('modelrank','D0002',2)
#redis.zadd('modelrank','D0003',1)
#從有序排列中取出最大值  ，用 zcard 取出序列共有將筆資料 ，因為在ZSET 中 最大的值會在愈後面，只要取出最大列就是前幾名
#higher=redis.zcard('modelrank')
#print(higher)
#然後用 zrangebyscore 取出最高排名的人
#modelclicklist=redis.zrangebyscore('modelrank',min=1,max='+inf', withscores=True)
#print(type(modelclicklist))
#print(modelclicklist[(higher -1)])
#print(redis.zrangebyscore('modelrank',min=1,max='+inf', withscores=True))

''' 輸出的結果
<type 'list'>
('D0002', 2.0)
[('D0001', 1.0), ('D0003', 1.0), ('D0002', 2.0)]
'''
#print(redis.zrange('modelrank',0,3)) #列出有序序列的結果
#print(redis.zrank('modelrank','D0002'))
#print(redis.zscore('modelrank','D0001')) #列出 分數 結果為1.0 SCORES
#print(redis.zincrby('modelrank','D0001',1)) #將序列成員加1分，結果為2分
'''
['D0001', 'D0003', 'D0002']
2
1.0
2.0



'''