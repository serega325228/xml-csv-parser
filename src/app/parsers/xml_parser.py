from collections.abc import Generator
from pathlib import Path

from lxml import etree


class XMLParser:
    def parse(self, path: Path) -> Generator[dict]:
        context = etree.iterparse(
            path,
            events=("end",),
            tag="item",
        )

        for _, elem in context:
            if elem.tag != "item":
                continue
            yield elem.attrib
            elem.clear()

            while elem.getprevious() is not None:
                del elem.getparent()[0]
