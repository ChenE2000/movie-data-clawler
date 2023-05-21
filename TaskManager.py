import random
import time
import json
import Clawler.DouBan as DouBan
import Clawler.MaoYan as MaoYan
from Clawler.Infrastructure import generate_movie_titles_todo_list, generate_movie_todo_list_by_redis, generate_celebrity_name, generate_celebrity_todo_list_by_redis

from DB.Context import redisDB as db_ctx

def get_all_movies_id():
    """ 爬取所有电影在各个网站的id """
    # generate movie titles todo list
    while len(generate_movie_titles_todo_list()) > 0:
        movie_titles_todo_list = generate_movie_titles_todo_list()
        movie = random.choice(movie_titles_todo_list)
        print("get ids from sites:", movie.title)
        movie.id_DouBan = DouBan.get_movie_id_by_title(movie.title)
        movie.id_MaoYan = MaoYan.get_movie_id_by_title(movie.title)
        movie.save_to_json()
        time.sleep(1)


def movies():
    todos = generate_movie_todo_list_by_redis()
    print("剩余任务:", len(todos))
    
    while len(todos) > 0:
        time.sleep(1)
        movie = random.choice(todos)
        if db_ctx.exist(movie.id_DouBan):
            print(f"已爬取<{movie.title}>, 跳过")
            todos.remove(movie)
        else:
            try:
                movie.clawler_action()
                data = movie._to_dict()
                db_ctx.set(str(movie.id_DouBan), json.dumps(data, ensure_ascii=False))
            except Exception as e:
                print(f"[ERROR] {e}")
                # time.sleep(2)
                continue
            
            
def celebrity():
    todo = generate_celebrity_todo_list_by_redis()
    
    for item in todo:
        time.sleep(2)
        print("正在爬取:", item['name'])
        if db_ctx.exist(item['uid']):
            print(f"已爬取<{item['name']}>, 跳过")
            continue
        else:
            try:
                cid = MaoYan.get_celebrity_id_by_name(item['name'])
                if cid == -1:
                    db_ctx.set(str(item['uid']), json.dumps({"姓名": item['name'], "uid": item['uid'], "exist":False}, ensure_ascii=False))
                    continue
                data = {
                    "姓名": item['name'],
                    "uid": item['uid'],
                    "总票房": MaoYan.get_celebrity_boxoffice(cid),
                    "获奖详情": MaoYan.get_celebrity_awards(cid),
                }
                db_ctx.set(str(item['uid']), json.dumps(data, ensure_ascii=False))
            except Exception as e:
                print(f"[ERROR] {e}")
                continue

if __name__ == "__main__":
    print("Start crawling")
    celebrity()
    
