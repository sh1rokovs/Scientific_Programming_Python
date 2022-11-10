import math as m


def get_objects():
    new_list = [[], dict(), 1, 'hi', 2.1, True, tuple(), set(), type, None, bytearray(), bytes(), 3 + 4j,
            FloatingPointError(), range(4, 5), reversed('hi'), object(), property(), GeneratorExit(), FutureWarning(),
            frozenset(), filter(None, 'hi'), FileNotFoundError(), FileExistsError(), Exception(),
            classmethod(None), EnvironmentError(), DeprecationWarning(), slice('hi'), staticmethod(None), zip(),
            EOFError(), map('hi', 'it'), memoryview(b'abc'), enumerate(b'abc'), iter('abc'), get_objects,
            ValueError(), NameError(), TypeError(), (x for x in range(1, 2)), m, str.title, iter([]), iter({}),
            iter(set()), dir]

    return sorted(new_list, key=lambda x: str(type(x)))

get_objects()
