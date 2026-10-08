from collections.abc import Callable
from pathlib import Path

from src.app.parsers.parser_provider import ParserProvider
from src.app.services.analyzer import AnalysisResult, Analyzer


class CLI:
    def __init__(
        self,
        parsers: dict[str, Callable[[], ParserProvider]],
        analyzer: Analyzer,
    ) -> None:
        self.parsers = parsers
        self.analyzer = analyzer

    def run(self) -> None:
        while True:
            print("0. Exit")
            print("1. Parse XML or CSV file")
            user_input = input("Enter your choice: ")
            if user_input == "0":
                break
            if user_input == "1":
                self._parse_file()
            else:
                print("Invalid choice")

    def _parse_file(self) -> None:
        path = Path(input("Enter the path to the XML/CSV file: "))
        if not path.is_file():
            print("File not found")
            return

        parser_factory = self.parsers.get(path.suffix.lower())
        if parser_factory is None:
            print("Invalid file type")
            return

        parser = parser_factory()
        result = self.analyzer.get_statistics(parser.parse(path))
        self._show_results(result)

    @staticmethod
    def _show_results(result: AnalysisResult) -> None:
        print("\n\nDUPLICATE RECORDS\n")
        print(result.duplicates)

        print("\n\nFLOORS PER CITY\n")
        for city, floors in result.floors_by_city.items():
            print(f"{city}: {floors}")

        print("\n\nTIME TAKEN\n")
        print(f"{result.elapsed_seconds:.2f}\n\n")
