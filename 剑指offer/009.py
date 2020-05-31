class CQueue:

    def __init__(self):
        self.a = []
        self.b = []

    def appendTail(self, value):
        self.a.append(value)

    def deleteHead(self):
        if self.b:
            return self.b.pop()
        if not self.a:
            return -1
        while self.a:
            self.b.append(self.a.pop())
        return self.b.pop()
