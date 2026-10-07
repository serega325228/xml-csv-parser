from collections.abc import Generator
from csv import DictReader
from pathlib import Path


class CSVParser:
    def parse(self, path: Path) -> Generator[dict]:
        with open(path, newline="", encoding="utf-8", mode="r") as f:
            reader = DictReader(f, delimiter=";")
            yield from reader
