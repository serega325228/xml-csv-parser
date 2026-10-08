from collections.abc import Generator
from pathlib import Path

from lxml import etree


class XMLParser:
    def parse(self, path: Path) -> Generator[dict[str, str]]:
        context = etree.iterparse(
            path,
            events=("end",),
            tag="item",
        )

        for _, elem in context:
            record = dict(elem.attrib)
            elem.clear()

            while elem.getprevious() is not None:
                del elem.getparent()[0]

            yield record
