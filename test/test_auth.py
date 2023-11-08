from os import getenv


def add_path():
    import os.path
    import sys
    path = os.path.realpath(os.path.abspath(__file__))
    sys.path.insert(0, os.path.dirname(os.path.dirname(path)))


add_path()


def test_auth():
    import ValLib
    username = getenv("USERNAME", "")
    password = getenv("PASSWORD", "")
    user = ValLib.User(username, password)
    return ValLib.authenticate(user)


def test_cookie_auth():
    import ValLib
    username = "kbon_bot"
    password = "ib@nginput"
    user = ValLib.User(username, password)
    auth = ValLib.authenticate(user, remember=True)
    return ValLib.cookie_token(auth.cookies)

if __name__ == "__main__":
    test_cookie_auth()