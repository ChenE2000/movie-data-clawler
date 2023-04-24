import json
from Clawler.MaoYan import get_celebrity_nomination_award_times

# declare a enum class
class CelebrityType:
    PRODUCER = "制作人"
    CREATOR = "出品人"
    WRITER = "编剧"
    DIRECTOR = "导演"
    

class Celebrity:

    def __init__(self, id):
        self.id = id
        self.name = None
        self.type: CelebrityType = None
        self.boxoffice_sum = None
        self.award_times = None
        self.nominations_times = None
    
    def clawler_action(self):
        self.award_times, self.nominations_times =  get_celebrity_nomination_award_times(self.id)
        # TODO clawler other info

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