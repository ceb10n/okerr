import pytest

from okerr import Ok, Result, UnwrapErr


def test_ok_val():
    ok = Ok('Success')

    assert ok.value == 'Success'


def test_ok_eq():
    ok = Ok('Success')
    ok1 = Ok('Success')

    assert ok == ok1
    assert not (ok == 'Success')


def test_ok_hash():
    ok = Ok('Success')
    ok1 = Ok('Success')

    assert ok.__hash__() == ok1.__hash__()


def test_ok_ne():
    ok = Ok('Success')
    ok2 = Ok('Ok return')

    assert ok != 'Success'
    assert ok != ok2


def test_ok_repr():
    ok = Ok('Success')

    assert repr(ok) == "Ok('Success')"


def test_ok_str():
    ok = Ok('Success')

    assert str(ok) == 'Ok: Success'


def test_ok_contains():
    ok = Ok('Success')

    assert ok.contains('Success') is True


def test_ok_contains_err():
    ok = Ok('Success')

    assert ok.contains_err('Some err') is False


def test_ok_expect():
    ok = Ok('Success')

    assert ok.expect('Some err') == 'Success'


def test_ok_is_err():
    ok = Ok('Success')

    assert ok.is_err() is False


def test_ok_is_ok():
    ok = Ok('Success')

    assert ok.is_ok() is True


def test_ok_unwrap():
    ok = Ok('Success')

    assert ok.unwrap() == 'Success'


def test_ok_unwrap_err():
    ok = Ok('Success')

    with pytest.raises(UnwrapErr):
        ok.unwrap_err()


def test_ok_unwrap_or():
    ok = Ok('Success')

    assert ok.unwrap_or('Alternative Success') == 'Success'


def test_ok_cls():
    ok = Ok('Success')

    assert isinstance(ok, Result) is True
    assert isinstance(ok, Ok) is True
