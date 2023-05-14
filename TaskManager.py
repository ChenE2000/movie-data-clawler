import random
import time
import json
from Clawler.DouBan import get_movie_id_by_title as get_movie_id_by_title_DouBan
from Clawler.MaoYan import get_movie_id_by_title as get_movie_id_by_title_MaoYan
from Clawler.Infrastructure import generate_movie_titles_todo_list, generate_movie_todo_list_by_redis

from DB.Context import redisDB as db_ctx

def get_all_movies_id():
    """ 爬取所有电影在各个网站的id """
    # generate movie titles todo list
    while len(generate_movie_titles_todo_list()) > 0:
        movie_titles_todo_list = generate_movie_titles_todo_list()
        movie = random.choice(movie_titles_todo_list)
        print("get ids from sites:", movie.title)
        movie.id_DouBan = get_movie_id_by_title_DouBan(movie.title)
        movie.id_MaoYan = get_movie_id_by_title_MaoYan(movie.title)
        movie.save_to_json()
        time.sleep(1)


def main():
    todos = generate_movie_todo_list_by_redis()
    
    while len(todos) > 0:
        time.sleep(3)
        movie = random.choice(todos)
        if db_ctx.exist(movie.id_DouBan):
            todos.remove(movie)
        else:
            try:
                movie.clawler_action()
                data = movie._to_dict()
                db_ctx.set(str(movie.id_DouBan), json.dumps(data, ensure_ascii=False))
            except Exception as e:
                print(e)
                time.sleep(2)
                continue

if __name__ == "__main__":
    print("Start crawling")
    main()
    
