from format_price import format_price
import pytest

@pytest.mark.parametrize("price, res", [('1234', '1 234.00'),
                                        ('3579871292.1', '3 579 871 292.10'),
                                        ('99.991654654321531', '99.99'),
                                        ('99.999', '100.00'),
                                        ('0.999', '1.00'),
                                        ('0.0019', '0.00'),
                                        ('3 579 871 292.10', '3 579 871 292.10'),
                                        ('0', '0.00'),
                                        ('-0.999', '-1.00'),
                                        ('!34%', '!34%'),
                                        ('qw', 'qw'),
                                        ('False', 'False')])
def test_format_price(price, res):
    assert format_price(price) == res
