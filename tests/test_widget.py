import pytest

from src.widget import get_data, mask_account_card


@pytest.fixture
def date():
    return "2024-08-03T17:26:18.671407"


def test_get_data(date):
    assert get_data(date) == "03.08.2024"


@pytest.mark.parametrize(
    "string, expected_result",
    [("MasterCard 1596837868705199", "MasterCard 1596 83** **** 5199"), ("Счет 64686473678894779589", "Счет **9589")],
)
def test_mask_account_card(string, expected_result):
    assert mask_account_card(string) == expected_result
