from okerr import Err, Ok, Match


def divide(a, b):
    try:
        return Ok(a / b)
    except ZeroDivisionError:
        return Err('Oh no, a ZeroDivisionError just happened')


if __name__ == '__main__':
    first_number = int(input('Please, inform an integer \n'))
    second_number = int(input('Please, inform another integer \n'))

    result = divide(first_number, second_number)

    Match(result) \
        .ok(lambda: print(result.value)) \
        .err(lambda: print(result.value))
