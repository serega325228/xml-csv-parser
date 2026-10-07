import time
from collections.abc import Generator


class Analyzer:
    def get_statistics(self, data: Generator[dict]) -> list[float | list | dict]:
        start_time = time.perf_counter()
        repeats = {}
        floors_in_city = {}
        for item in data:
            city = item["city"]
            key = "".join(item.values())
            if key in repeats:
                repeats[key][1] += 1
            else:
                floor = item["floor"]
                repeats[key] = [item, 1]
                if city not in floors_in_city:
                    floors_in_city[city] = [0] * 5
                floors_in_city[city][int(floor) - 1] += 1

        repeats = [repeat for repeat in repeats.values() if repeat[1] > 1]

        end_time = time.perf_counter()
        return [repeats, floors_in_city, end_time - start_time]
