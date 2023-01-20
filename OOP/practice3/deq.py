class Lists:
    values = None
    current = -1

    def __init__(self, length=10):
        self.values = [None] * length

    def push(self, value):
        if abs(self.current) >= len(self.values):
            new_values = [None] * len(self.values) * 2
            for i in range(len(self.values)):
                new_values[-1 - i] = self.values[-1 - i]
            self.values = new_values

        self.values[self.current] = value
        self.current -= 1

    def pop(self):
        if self.current > -1:
            return None

        out = self.values[self.current]
        self.values[self.current] = None
        self.current += 1
        return out

    def clear(self):
        self.values = [None] * 10
        self.current = -1

    def show(self):
        return self.values


if __name__ == '__main__':
    deq = Lists(5)
    print(deq.values)

    for i in range(10):
        deq.push(i)
        print(deq.values)

    for i in range(15):
        deq.pop()
        print(deq.values)
