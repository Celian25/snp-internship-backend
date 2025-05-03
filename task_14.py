class EvenNumbers:
    def __init__(self, n: int):
        self.cur = 0
        self.count = 0
        self.stop = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.stop:
            raise StopIteration

        x = self.cur
        self.cur += 2
        self.count += 1
        return x


evens = EvenNumbers(5)

for i in evens:
    print(i)
