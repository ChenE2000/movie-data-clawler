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
        self.commercial_value = None
        self.endorsement_value = None
        self.heat_value = None
        self.praise_value = None
        self.major_value = None

    def clawler_action(self):
        self.id = {
            # "猫眼": self.id,
            "艾漫": AiMan.get_movie_id_by_title(self.name),
            "时光": ShiGuang.get_celebrity_id_by_name(self.name),
        }

        award_times, nominations_times = MaoYan.get_celebrity_nomination_award_times(self.id["猫眼"])
        self.MaoYan["获奖"] = {
            "获奖详情": MaoYan.get_celebrity_awards(self.id["猫眼"]),
            "获奖次数": award_times,
            "提名次数": nominations_times
        }
        
        AiMan_data = AiMan.main_processes(self.name)
        self.commercial_value = AiMan_data['商业价值']
        self.endorsement_value = AiMan_data['代言指数']
        self.heat_value = AiMan_data['热度指数']
        self.praise_value = AiMan_data['口碑指数']
        self.major_value = AiMan_data['专业指数']


    def _to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "type": self.type,
            "boxoffice_sum": self.boxoffice_sum,
            "award_times": self.award_times,
            "nominations_times": self.nominations_times,
            "商业价值": self.commercial_value,
            "代言指数": self.endorsement_value,
            "热度指数": self.heat_value,
            "口碑指数": self.praise_value,
            "专业指数": self.major_value
        }

    def save_to_json(self, root_path: str = "./data/celebrity/"):
        path = root_path + self.id + ".json"
        with open(path, "w", encoding="utf-8") as f:
            json.dump(self._to_dict(), f, ensure_ascii=False)
