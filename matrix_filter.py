from itertools import accumulate


class score_filter:

    def __init__(self, min_score, max_score):
        self.result = None
        self.min_score = min_score
        self.max_score = max_score

    def fit(self, x, y, obj_iter):
        x = list(accumulate(x))
        y = list(accumulate(y))
        self.result = [(el, elem) for el, elem in obj_iter
                       if self.min_score < (x[el] * y[elem]) / (x[len(x) - 1] * y[len(y) - 1]) < self.max_score]
        return self

    def __iter__(self):
        return (el for el in self.result)
