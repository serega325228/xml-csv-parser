import time
from collections.abc import Iterable
from dataclasses import dataclass

Record = dict[str, str]
RecordKey = tuple[str, str, str, str]


@dataclass(frozen=True, slots=True)
class AnalysisResult:
    duplicates: list[tuple[Record, int]]
    floors_by_city: dict[str, list[int]]
    elapsed_seconds: float


class Analyzer:
    def get_statistics(self, data: Iterable[Record]) -> AnalysisResult:
        start_time = time.perf_counter()
        seen: set[RecordKey] = set()
        duplicate_counts: dict[RecordKey, int] = {}
        floors_by_city: dict[str, list[int]] = {}

        for item in data:
            city = item["city"]
            street = item["street"]
            house = item["house"]
            floor = item["floor"]
            key = (city, street, house, floor)

            floor_number = int(floor)
            if not 1 <= floor_number <= 5:
                raise ValueError(f"Floor must be between 1 and 5, got {floor!r}")
            floors_by_city.setdefault(city, [0] * 5)[floor_number - 1] += 1

            if key in seen:
                duplicate_counts[key] = duplicate_counts.get(key, 1) + 1
            else:
                seen.add(key)

        duplicates = [
            (
                {"city": city, "street": street, "house": house, "floor": floor},
                count,
            )
            for (city, street, house, floor), count in duplicate_counts.items()
        ]

        return AnalysisResult(
            duplicates=duplicates,
            floors_by_city=floors_by_city,
            elapsed_seconds=time.perf_counter() - start_time,
        )
