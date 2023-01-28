class Expressions:

    def __init__(self):
        self.history = {}
        self.current = 0

    def append(self, results: tuple):
        self.history.update({self.current: {'answer': results[1], 'expression': results[0]}})
        self.current += 1

