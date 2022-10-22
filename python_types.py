def get_objects():
    return [False, b'', {}, 1.1, 1, [], None, {"a", "b"}, 'str', ()]


for el in get_objects():
    print(type(el))
