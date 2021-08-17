import re


def longest_password(password: str) -> int:
    words = password.split()
    max_length = -1
    for word in words:
        if all([
            re.match("^[0-9a-zA-Z]*$", word),
            len(re.sub("[0-9]+", "", word)) % 2 == 0,
            len(re.sub("[a-zA-Z]+", "", word)) % 2 == 1,
        ]):
            max_length = max(max_length, len(word))

    return max_length
