def cmp_to_key(comparator):
    class MyClass:
        def __init__(self, value):
            self.value = value

        def __lt__(self, other):
            return comparator(self.value, other.value) == -1

    return MyClass
