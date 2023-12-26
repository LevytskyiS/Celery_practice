import redis

REDIS_HOST = "localhost"
REDIS_PORT = 6379

with redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True) as client:
    while True:
        problem = input("::: ")  # 2 - 5
        client.lpush("problems", problem)
        answer = client.brpop("answers")[1]
        print("ANSWER: ", answer)

# Можно перейти в терминал контейнера в докере и ввести redis-cli
# Потом ввести KEYS *, чтобы проверить все ключи
# И в данном случае, еще ввести комманду LRANGE problems 0 100,
# чтобы увидеть значения сохраненные под ключем problems
