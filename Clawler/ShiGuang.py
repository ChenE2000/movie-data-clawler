import requests
import json
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",

}


def get_top_10_000_movies():
    url = "http://front-gateway.mtime.com/mtime-search/search/unionSearch2"
    batch = []

    for page in range(10):
        print(f"page: {page+1}")
        req = requests.post(url, data={
            "keyword": "",
            "pageIndex": page+1,
            "pageSize": 1000,
            "searchType":0,
            "locationId":290,
            "genreTypes":"",
            "area":"中国",
            "year":""
        }, headers=headers).json()
        batch.extend(req["data"]["movies"])
        time.sleep(5)
    
    return batch


if __name__ == "__main__":
    res = get_top_10_000_movies()
    # save to json
    with open("./10_000_movies.json", "w", encoding="utf-8") as f:
        json.dump(res, f, ensure_ascii=False)