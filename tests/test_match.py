from okerr import Err, Match, Ok


def ok_op(msg: str):
    return f'Ok: {msg}'


def err_op(msg: str):
    return f'Err: {msg}'


def op_without_arg():
    return 'err_op_without_arg'


def op_with_args(*args):
    return 'op_with_args'


def op_with_kwargs(**kwargs):
    return 'op_with_kwargs'


def test_match_ok():
    msg = 'Okdok'
    return_ok = Match(Ok('Success')) \
        .ok(ok_op, msg) \
        .collect()

    assert return_ok == ok_op(msg)


def test_match_err():
    msg = 'Nopop'
    return_err = Match(Err('Err')) \
        .err(err_op, msg) \
        .collect()

    assert return_err == err_op(msg)


def test_match_ok_without_arg():
    return_ok = Match(Ok('Success')) \
        .ok(op_without_arg) \
        .collect()

    assert return_ok == op_without_arg()


def test_match_ok_with_args():
    return_ok = Match(Ok('Success')) \
        .ok(op_with_args, 1, 2, 3, 4, 5) \
        .collect()

    assert return_ok == op_with_args()


def test_match_ok_with_kwargs():
    return_ok = Match(Ok('Success')) \
        .ok(op_with_kwargs, a=1, b=2, c=3, d=4, e=5) \
        .collect()

    assert return_ok == op_with_kwargs()


def test_match_return_none_with_no_op():
    return_ok = Match(Ok('Success')) \
        .ok(None) \
        .collect()

    assert return_ok is None
