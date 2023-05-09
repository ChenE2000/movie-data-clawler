import random
import time
from Clawler.DouBan import get_movie_id_by_title as get_movie_id_by_title_DouBan
from Clawler.MaoYan import get_movie_id_by_title as get_movie_id_by_title_MaoYan
from Clawler.Infrastructure import generate_movie_titles_todo_list


def get_all_movies_id():
    """ 爬取所有电影在各个网站的id """ 
    # generate movie titles todo list
    while len(generate_movie_titles_todo_list())>0:
        movie_titles_todo_list = generate_movie_titles_todo_list()
        movie = random.choice(movie_titles_todo_list)
        print("get ids from sites:", movie.title)
        movie.id_DouBan = get_movie_id_by_title_DouBan(movie.title)
        movie.id_MaoYan = get_movie_id_by_title_MaoYan(movie.title)
        movie.save_to_json()
        time.sleep(1)
        
if __name__ == "__main__":
    print("Start crawling")
    get_all_movies_id()

    