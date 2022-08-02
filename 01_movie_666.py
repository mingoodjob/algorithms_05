N = 187
movie_name = 0

for i in range(1, N+1):
    while True:
        movie_name += 1
        if "666" in str(movie_name):
            break

print(movie_name)