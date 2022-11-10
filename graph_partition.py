class graph_partition:
    def __init__(self, process_id, process_amount):
        self.var_a = None
        self.var_b = None
        self.processes = None
        self.graph_vert_amount = None
        self.process_id = process_id
        self.process_amount = process_amount
        self.current = -1

    def fit(self, graph_vert_amount):
        self.graph_vert_amount = graph_vert_amount
        summary = 0
        for el in range(graph_vert_amount):
            summary += el
        div = summary // self.process_amount
        mod = summary % self.process_amount
        for el in range(self.process_amount):
            self.processes.append(div)
        for el in range(mod):
            self.processes[el] += 1

        process_id = 0
        for el in range(len(self.processes[:self.process_id])):
            process_id += el
        num = graph_vert_amount - 2
        for j in range(0, graph_vert_amount - 1):
            if process_id - 1 <= num:
                self.var_a, self.var_b = j, graph_vert_amount - 1 - num + process_id - 1
                break
            else:
                num += (graph_vert_amount - 2 - j)
        return self

    def __len__(self):
        return self.processes[self.process_id]

    def __next__(self):
        self.current += 1
        if self.current < self.__len__():
            current = self.var_b + 1
            if current < self.graph_vert_amount:
                self.var_b = current
            else:
                self.var_a = self.var_a + 1
                self.var_b = self.var_a + 2
            return tuple((self.var_a, self.var_b))

    def __iter__(self):
        return self


nw = graph_partition(2, 3)
