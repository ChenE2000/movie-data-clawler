import time
from Celebrity import Celebrity
from Clawler.DouBan import get_movie_id_by_title as get_movie_id_by_title_DouBan
from Clawler.MaoYan import get_movie_id_by_title as get_movie_id_by_title_MaoYan
from Clawler.Infrastructure import generate_movie_titles_todo_list

if __name__ == "__main__":
    
    # generate movie titles todo list
    movie_titles_todo_list = generate_movie_titles_todo_list()
    
    for movie in movie_titles_todo_list[0:3]:
        movie.id_DouBan = get_movie_id_by_title_DouBan(movie.title)
        movie.id_MaoYan = get_movie_id_by_title_MaoYan(movie.title)
        movie.save_to_json()
        time.sleep(2)

    