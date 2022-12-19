import redis
import os

redis_location=os.environ["REDIS_LOCATION"]
redis_port=os.environ["REDIS_PORT"]
redis_cli = redis.Redis(host=redis_location, port=redis_port, db=0)


def contador_visitas():
    redis_cli.incr('num_visitas')
    visitas = redis_cli.get('num_visitas')
    return visitas.decode("utf-8")