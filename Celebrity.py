import json
import Clawler.AiMan as AiMan
import Clawler.ShiGuang as ShiGuang
import Clawler.DouBan as DouBan


# declare a enum class
class CelebrityType:
    PRODUCER = "制作人"
    CREATOR = "出品人"
    WRITER = "编剧"
    DIRECTOR = "导演"
    

class Celebrity:

    def __init__(self, name):
        self.name = name
        self.type: CelebrityType = None
        self.boxoffice_sum = None
        self.award_times = None
        self.nominations_times = None
    
    def clawler_action(self):
        
        award_times, nominations_times = MaoYan.get_celebrity_nomination_award_times(self.id["猫眼"])
        self.MaoYan["获奖"] = {
            "获奖详情": MaoYan.get_celebrity_awards(self.id["猫眼"]),
            "获奖次数": award_times,
            "提名次数": nominations_times
        }


    def _to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "type": self.type,
            "boxoffice_sum": self.boxoffice_sum,
            "award_times": self.award_times,
            "nominations_times": self.nominations_times
        }

    def save_to_json(self, root_path: str = "./data/celebrity/"):
        path = root_path + self.id + ".json"
        with open(path, "w", encoding="utf-8") as f:
            json.dump(self._to_dict(), f, ensure_ascii=False)