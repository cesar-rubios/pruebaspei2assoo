docker network create mynet
docker run --net mynet --name redisserver -d redis
docker run --net mynet -it redis redis-cli -h redisserver
redisserver:6379>