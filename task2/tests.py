import pytest

from main import parse, DATA

@pytest.mark.parametrize(
    "input,result",
    [
        (
            DATA, 
            {
                'X Æ A-12': {'hours': [45], 'sum': 45},
                'Андрей': {'hours': [9, 6], 'sum': 15},
                'Василий': {'hours': [11], 'sum': 11},
                'Иван Петров': {'hours': [3], 'sum': 3},
                'Роман': {'hours': [7, 11], 'sum': 18},
            },
        ),
    ]
)
def test_parser(input: str, result: dict):
    assert parse(input) == result