import re
import difflib


def find_closest_match(title, titles):
    """ 
    find the closest match title from a list of titles
    return: the closest match title
    """
    # remove space and special characters
    title = re.sub(r'[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）]+', '', title)
    # find the closest match title
    match_title = difflib.get_close_matches(title, titles, 1, 0.5)
    if match_title:
        # return index of the closest match title
        return titles.index(match_title[0])
    else:
        return None
