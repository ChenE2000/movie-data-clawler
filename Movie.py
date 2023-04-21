import json


class Movie:

    def __init__(self, title):

        self.title = title
        self.id_IMDb = None
        self.id_MaoYan = None
        self.id_DouBan = None
        self.id_ShiGuang = None
    
    def _to_dict(self):
        return {
            "title": self.title,
            "id_IMDb": self.id_IMDb,
            "id_MaoYan": self.id_MaoYan,
            "id_DouBan": self.id_DouBan,
            "id_ShiGuang": self.id_ShiGuang
        }
 
    def save_to_json(self, root_path: str = "./metadata/merged/"):
        path = root_path + self.title + ".json"
        with open(path, "w", encoding="utf-8") as f:
            json.dump(self._to_dict(), f, ensure_ascii=False)

    