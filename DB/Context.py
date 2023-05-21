import redis
import json

class RedisDB:

    def __init__(self):
        self.redis = redis.Redis(host='101.35.159.111', port=6388, db=2, password="CODE6388code6388")

    def set(self, key, value):
        self.redis.set(key, value)

    def get(self, key):
        return self.redis.get(key).decode("utf-8")

    def exist(self, key):
        return self.redis.exists(key)
    
    def delete(self, key):
        return self.redis.delete(key)

    def get_all_keys(self):
        keys = self.redis.keys()
        # convert to int
        keys = list(map(lambda x: int(x.decode("utf-8")), keys))
        return keys

    def get_all_objects(self):
        keys = self.get_all_keys()
        return list(map(lambda x: (x, self.get(x)), keys))

    def clear_db(self):
        self.redis.flushdb()
        print("clear db")

    def key_count(self):
        return len(self.redis.keys())
    
redisDB = RedisDB()

if __name__ == "__main__":
    print(len(redisDB.get_all_keys()))
    
    # for key in redisDB.get_all_keys():
    #     if redisDB.get(key) == '-':
    #         redisDB.delete(key)
    #         print("delete key: ", key)
            
    all_data = redisDB.get_all_objects()
    res = []
    for item in all_data:
        res.append(json.loads(item[1]))
    
    res.sort(key=lambda x: x["uid"])
    
    with open("./celebrity_MaoYan.json", "w", encoding="utf-8") as f:
        json.dump(res, f, ensure_ascii=False, indent=4)
        
