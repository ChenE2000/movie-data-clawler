import json
import typing
from Movie import Movie

def generate_movie_titles_todo_list() -> typing.List[Movie]:
    """ 生成电影标题待爬取列表,以时光网数据为基准 """
    batch = []
    with open('./metadata/ShiGuang/10_000_movies.json', 'r', encoding='utf-8') as f:
        movies = json.load(f)
        for item in movies:
            movie = Movie(title=item["name"])
            movie.id_ShiGuang = item["movieId"]
            batch.append(movie)

    return batch
