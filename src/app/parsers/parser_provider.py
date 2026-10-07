from collections.abc import Generator
from pathlib import Path
from typing import Protocol


class ParserProvider(Protocol):
    def parse(self, path: Path) -> Generator[dict[str, str]]:
        ...
