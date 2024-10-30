DATA = """
Андрей 9
Василий 11
Роман 7
X Æ A-12 45
Иван Петров 3
Андрей 6
Роман 11
"""

def _parse_row(row: str) -> tuple[str, dict[str, int]]:
    name, hours = row.rsplit(" ", maxsplit=1)
    data = {
        "hours": [int(hours)],
        "sum": int(hours),
    }

    return name, data

def parse(data: str) -> dict[str, dict[str, int | list[int]]]:
    parsed_data = {}

    for row in data.splitlines():
        if not row:
            # пропуск пустых строк
            continue
        
        name, data = _parse_row(row)
        if name not in parsed_data:
            parsed_data[name] = data
        else:
            parsed_data[name]["hours"].extend(data["hours"])
            parsed_data[name]["sum"] = sum( parsed_data[name]["hours"])

    return parsed_data


{
    'X Æ A-12': {'hours': [45], 'sum': 45},
    'Андрей': {'hours': [9, 6], 'sum': 15},
    'Василий': {'hours': [11], 'sum': 11},
    'Иван Петров': {'hours': [3], 'sum': 3},
    'Роман': {'hours': [7, 11], 'sum': 18},
}