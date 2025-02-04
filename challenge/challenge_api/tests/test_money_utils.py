import pytest

from challenge_api.utils import money as util

@pytest.mark.parametrize(
    'currency, expected',
    [
        ('M', 1200000),
        ('K', 1200),
    ]
)
def test_num_from_currency(currency, expected):
    assert util.num_from_currency(f'$1.2{currency}') == expected


@pytest.mark.parametrize(
    'value',
    [
        '$1.2',
        '$1.2B',
        '$1.2T',
    ]
)
def test_num_from_currency_invalid_suffix(value):
    with pytest.raises(ValueError):
        util.num_from_currency(value)
