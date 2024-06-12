class Embedding:
    def __init__(self, inputs):
        o = self.embedding(inputs)
        o += self.positional_encoding(o)
        return o

    def embedding(self):
        return

    def positional_encoding(self):
        return