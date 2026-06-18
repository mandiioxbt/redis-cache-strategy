class CacheAside:
    def __init__(self, redis_client): self.r = redis_client
    def get_or_set(self, key, fn, ttl=3600):
        v = self.r.get(key)
        if v: return v
        v = fn(); self.r.setex(key, ttl, v); return v

class WriteThrough:
    def __init__(self, redis_client, db): self.r, self.db = redis_client, db
    def write(self, key, val, ttl=3600): self.db.write(key, val); self.r.setex(key, ttl, val)
    def read(self, key):
        v = self.r.get(key)
        if v: return v
        v = self.db.read(key)
        if v: self.r.setex(key, 3600, v)
        return v
