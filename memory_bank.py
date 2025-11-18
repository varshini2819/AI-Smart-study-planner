class MemoryBank:
    def __init__(self):
        self.storage = []

    def save(self, data):
        self.storage.append(data)

    def get_all(self):
        return self.storage
