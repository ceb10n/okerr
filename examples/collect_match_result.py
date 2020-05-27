from okerr import Err, Ok, Match


class User:

    def __init__(self, username):
        self.username = username

    def __str__(self):
        return f"I'm {username} and I'm authenticated ;)"


def authenticate(username, password):
    if username == 'ok' and password == 'err':
        user = User(username)
        return Ok(user)

    return Err("You're not allowed here!")


def awesome_authenticated_stuff(user: User) -> User:
    return user


def awful_result(msg: str):
    return msg


if __name__ == '__main__':
    username = input('username: ')
    password = input('password: ')

    result = authenticate(username, password)

    collected_value = Match(result) \
        .ok(awesome_authenticated_stuff, result.value) \
        .err(awful_result, result.value) \
        .collect()

    print(collected_value)
