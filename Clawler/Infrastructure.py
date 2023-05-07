import os
import json
import typing
from Movie import Movie

def generate_movie_titles_todo_list() -> typing.List[Movie]:
    """ 生成电影标题待爬取列表,以时光网数据为基准 """
    existed = os.listdir('./metadata/merged/')
    
    batch = []
    with open('./metadata/ShiGuang/10_000_movies.json', 'r', encoding='utf-8') as f:
        movies = json.load(f)
        for item in movies:
            if item["name"] + ".json" in existed:
                # skip existed movies
                continue
            movie = Movie(title=item["name"])
            movie.id_ShiGuang = item["movieId"]
            batch.append(movie)

    if len(batch) == 0:
        raise Exception("No movie titles to crawl")
    print("Total movies to crawl: ", len(batch))
    return batch
