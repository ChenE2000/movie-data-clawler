import redis


class RedisDB:

    def __init__(self):
        self.redis = redis.Redis(host='101.35.159.111', port=6388, db=0, password="CODE6388code6388")

    def set(self, key, value):
        self.redis.set(key, value)

    def get(self, key):
        return self.redis.get(key)

    def exist(self, key):
        return self.redis.exists(key)

    def get_all_keys(self):
        return self.redis.keys()

    def get_all_objects(self):
        keys = self.get_all_keys()
        return list(map(lambda x: (x, self.get(x)), keys))

    def clear_db(self):
        self.redis.flushdb()


if __name__ == "__main__":
    r = RedisDB()
    # r.set("test", "test")
    print(r.get_all_keys())
    print(r.get_all_objects())
