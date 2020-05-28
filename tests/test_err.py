import pytest

from okerr import Err, Result, UnwrapErr


class TestErr:

    def setup_class(cls):
        cls.err = Err('Some err')
        cls.err1 = Err('Some err')
        cls.err2 = Err('Another err')

    def test_val(self):
        assert self.err.value == 'Some err'

    def test_eq(self):
        assert self.err == self.err1
        assert not (self.err == 'Some err')

    def test_hash(self):
        assert self.err.__hash__() == self.err1.__hash__()

    def test_ne(self):
        assert self.err != 'Some err'
        assert self.err != self.err2

    def test_repr(self):
        assert repr(self.err) == "Err('Some err')"

    def test_str(self):
        assert str(self.err) == 'Err: Some err'

    def test_contains(self):
        self.err.contains('Some err') is False

    def test_contains_err(self):
        assert self.err.contains_err('Some err') is True

    def test_expect(self):
        with pytest.raises(UnwrapErr):
            assert self.err.expect('Some err')

    def test_is_err(self):
        assert self.err.is_err() is True

    def test_is_ok(self):
        assert self.err.is_ok() is False

    def test_unwrap(self):
        with pytest.raises(UnwrapErr):
            self.err.unwrap()

    def test_unwrap_err(self):
        assert self.err.unwrap_err() == 'Some err'

    def test_unwrap_or(self):
        assert self.err.unwrap_or('Oh no!') == 'Oh no!'

    def test_cls(self):
        assert isinstance(self.err, Result) is True
        assert isinstance(self.err, Err) is True
