import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "string, expected_result",
    [
        ("1596837868705199", "1596 83** **** 5199"),
        ("6831982476737658", "6831 98** **** 7658"),
    ],
)
def test_get_mask_card_number(string, expected_result):
    assert get_mask_card_number(string) == expected_result


@pytest.mark.parametrize(
    "string, expected_result",
    [
        ("64686473678894779589", "**9589"),
        ("73654108430135874305", "**4305"),
    ],
)
def test_get_mask_account(string, expected_result):
    assert get_mask_account(string) == expected_result