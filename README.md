https://masteryi.notion.site/deeea7ea328b4f42b740320f5629d8ab

docker run -d --name movie-redis \
  -p 6388:6379 \
  -v ./redis-data:/data \
  -e REDIS_PASSWORD=CODE6388code6388 \
  redis redis-server --bind 0.0.0.0 --appendonly yes --requirepass $REDIS_PASSWORD


sudo docker compose up --abort-on-container-exit

# TODO
在使用搜索查找某电影ID时使用find_closest_match匹配title，这可能导致爬取的电影和预期不符，在后期需要调整