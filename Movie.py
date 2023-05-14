import json
import time
import Clawler.DouBan as DouBan
import Clawler.ShiGuang as ShiGuang
import Clawler.MaoYan as MaoYan

class Movie:

    def __init__(self, title, id_IMDb=None, id_MaoYan=None, id_DouBan=None, id_ShiGuang=None):
        self.title = title
        self.id_IMDb = id_IMDb
        self.id_MaoYan = id_MaoYan
        self.id_DouBan = id_DouBan
        self.id_ShiGuang = id_ShiGuang
        
        self.created_time = None

        self.DouBan = {}
        self.MaoYan = {}
        self.ShiGuang = {}

    # def set_boxoffice(self):
    #     self.MaoYan['票房'] = MaoYan.get_movie_boxoffice_by_id(self.id_MaoYan)
        
    def clawler_action(self):
        print(f"{self.title}正在爬取...")
        self.created_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        douban_subject = DouBan.get_movie_subject_by_id(self.id_DouBan)
        self.DouBan['基础信息'] = DouBan.get_movie_basic_info_by_subject(soup=douban_subject)
        self.DouBan['打分数据'] = DouBan.get_movie_rating_info_by_subject(soup=douban_subject)
        self.DouBan['感兴趣指数'] = DouBan.get_movie_interested_info_by_subject(soup=douban_subject)

        self.MaoYan['获奖情况'] = MaoYan.get_movie_awards_info_by_id(self.id_MaoYan)
        
        self.ShiGuang['打分数据'] = ShiGuang.get_movie_rating_info_by_id(self.id_ShiGuang)
        self.ShiGuang['拍摄技术'] = ShiGuang.get_movie_technique_by_id(id=self.id_ShiGuang)
    
    def _to_dict(self):
        return {
            "电影名称": self.title,
            "获取时间": self.created_time,
            "id": {
                "豆瓣": self.id_DouBan,
                "时光": self.id_ShiGuang,
                "猫眼": self.id_MaoYan
            },
            "豆瓣": self.DouBan,
            "时光": self.ShiGuang,
            "猫眼": self.MaoYan
        }

    def save_to_json(self, root_path: str = "./"):
        print("save movie: ", self.title, self._to_dict())
        path = root_path + self.title + ".json"
        with open(path, "w", encoding="utf-8") as f:
            json.dump(self._to_dict(), f, ensure_ascii=False, indent=4)
