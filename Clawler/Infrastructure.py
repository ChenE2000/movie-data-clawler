import os
import json
import typing
from Movie import Movie
from Celebrity import Celebrity
from DB.Context import redisDB as db_ctx

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


def generate_movie_todo_list_by_redis() -> typing.List[Movie]:
    """ 从redis中获取电影待爬取列表 """
    douban_ids = db_ctx.get_all_keys()
    todos = []
    print("Total movies crawled: ", len(douban_ids), douban_ids)
    
    path = "./metadata/movies_with_boxoffice.json"
    with open(path, "r", encoding="utf-8") as f:
        movies = json.load(f)
        for movie in movies:
            if movie["ids"]["id_DouBan"] in douban_ids:
                continue
            item = Movie(
                title=movie["title"], 
                id_DouBan=movie["ids"]["id_DouBan"], 
                id_MaoYan=movie["ids"]["id_MaoYan"], 
                id_ShiGuang=movie["ids"]["id_ShiGuang"]
                )
            item.MaoYan['票房'] = movie["profession_films_boxoffice"]
            todos.append(item)
    
    return todos            
    
    
def generate_celebrity_name():
    """ 生成演员待爬取列表 """
    path = "./metadata/all.json"
    with open(path, "r", encoding="utf-8") as f:
        movies = json.load(f)
        celebrities = []
        for movie in movies:
            if '导演' in movie['豆瓣']['基础信息']:
                celebrities += movie['豆瓣']['基础信息']['导演']
            if '编剧' in movie['豆瓣']['基础信息']:
                celebrities += movie['豆瓣']['基础信息']['编剧']
            if '主演' in movie['豆瓣']['基础信息']:
                celebrities += movie['豆瓣']['基础信息']['主演']
    
    deduped = list(set(celebrities))
    c_l = []
    # add incremental id to each celebrity
    for i, celebrity in enumerate(deduped):
        c_l.append({
            "uid": i,
            "name": celebrity
        })
        
    print("Total celebrities to crawl: ", len(c_l))
    return c_l


def generate_celebrity_todo_list_by_redis():
    keys = db_ctx.get_all_keys()
    with open("./metadata/celebrity_name.json", "r", encoding="utf-8") as f:
        celebrities = json.load(f)
        
        todo = list(filter(lambda x: x["uid"] not in keys, celebrities))
        print("Total celebrities to crawl: ", len(todo))
    return todo