from collections.abc import Callable

from src.app.cli.cli import menu
from src.app.parsers.csv_parser import CSVParser
from src.app.parsers.parser_provider import ParserProvider
from src.app.parsers.xml_parser import XMLParser
from src.app.services.analyzer import Analyzer


def main():
    print("Hello from XML/CSV parser!")
    providers: dict[str, Callable[[], ParserProvider]] = {
        ".xml": XMLParser,
        ".csv": CSVParser,
    }

    analyzer = Analyzer()
    menu(providers, analyzer)


if __name__ == "__main__":
    main()
