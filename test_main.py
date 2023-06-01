from main import get_name, get_address, get_mobile, get_email, inp
from unittest.mock import Mock, patch
from pytest import raises


def test_get_name() -> None:
    with patch("builtins.input", new=Mock(return_value="John Smith")):
        assert get_name() == "John Smith"


def test_get_address() -> None:
    with patch("builtins.input", new=Mock(return_value="123, Long Street, L12 3EY")):
        assert get_address() == "123, Long Street, L12 3EY"


def test_get_mobile() -> None:
    with patch("builtins.input", new=Mock(return_value="+440123456789")):
        assert get_mobile() == "+440123456789"
    with patch("builtins.input", new=Mock(return_value="+4401234567891")):
        with raises(AttributeError):
            get_mobile()


def test_get_email() -> None:
    with patch("builtins.input", new=Mock(return_value="hello@gmail.com")):
        assert get_email() == "hello@gmail.com"


def test_inp() -> None:
    with patch("builtins.input", new=Mock(return_value="c")):
        assert inp() == "C"
