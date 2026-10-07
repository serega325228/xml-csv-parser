from collections.abc import Callable
from pathlib import Path

from src.app.parsers.parser_provider import ParserProvider
from src.app.services.analyzer import Analyzer


def menu(parsers: dict[str, Callable[[], ParserProvider]], analyzer: Analyzer):
    while True:
        print("0. Exit")
        print("1. Parse XML or CSV file")
        user_input = input("Enter your choice: ")
        if user_input == "0":
            break
        elif user_input == "1":
            path = Path(input("Enter the path to the XML/CSV file: "))
            if not path.exists():
                print("File not found")
                continue
            if path.suffix in parsers:
                parser = parsers[path.suffix]()
                results = analyzer.get_statistics(parser.parse(path))
                show_results(results)
            else:
                print("Invalid file type")
                continue
        else:
            print("Invalid choice")

def show_results(results: list[dict | list | float]):
    print("\n\nDUPLICATE RECORDS\n")
    # for k, v in results[0]:
    #     print(f"{k}: {v}")
    print(results[0])

    print("\n\nFLOORS PER CITY\n")
    for city, floors in results[1].items():
        print(f"{city}: {floors}")

    print("\n\nTIME TAKEN\n")
    print(f"{results[2]:.2f}\n\n")
