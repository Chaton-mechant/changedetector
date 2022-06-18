import time

class Loader:
    def __init__(self):
        self.loader = self.purcent()

    def run(self):
        for i in self.loader:
            print(i, end="\r")
            time.sleep(0.005)

    def purcent(self):
        # generate a random list of strings of length 20
        for i in range(26):
            n = '⬜' * i
            yield f"""{i*4}% {n}"""
