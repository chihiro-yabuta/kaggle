from embedding import Embedding
from add_norm import AddNorm
from attention import MultiHeadAttention
from forward import FeedForward

class Encoder:
    def __init__(self, inputs):
        o = Embedding(inputs)
        o = AddNorm(o, MultiHeadAttention(o))
        o = AddNorm(o, FeedForward(o))
        return o