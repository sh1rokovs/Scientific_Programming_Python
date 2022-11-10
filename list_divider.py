class list_divider(list):

    def __init__(self, def_list):
        super().__init__()
        self.def_list = def_list

    def __truediv__(self, delimiter):
        if type(self.def_list) == list and type(delimiter) == int:
            if delimiter >= 1:
                return self.function_split(self.def_list, delimiter)

    @staticmethod
    def function_split(def_list, split_item):
        div = len(def_list) // split_item
        mod = len(def_list) % split_item
        new_list = []
        for el in range(split_item):
            a = el * div + min(el, mod)
            b = (el + 1) * div + min(el + 1, mod)
            new_list.append(new_list[a:b])
        return new_list
