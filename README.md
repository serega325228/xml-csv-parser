# XML/CSV Parser

## English

A streaming command-line parser for large XML and semicolon-separated CSV files. It finds duplicate address records, counts floors from 1 to 5 for each city, and reports processing time.

Run the application:

```bash
uv run python -m src.app.main
```

Choose option `1` and enter the path to an `.xml` or `.csv` file. XML records must use `item` elements; both formats require the fields `city`, `street`, `house`, and `floor`.

## Русский

Потоковый консольный парсер больших XML-файлов и CSV-файлов с разделителем `;`. Он находит повторяющиеся адреса, подсчитывает этажи с 1-го по 5-й для каждого города и показывает время обработки.

Запуск приложения:

```bash
uv run python -m src.app.main
```

Выберите пункт `1` и укажите путь к файлу `.xml` или `.csv`. В XML записи должны находиться в элементах `item`; для обоих форматов обязательны поля `city`, `street`, `house` и `floor`.
