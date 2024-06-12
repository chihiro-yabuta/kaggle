from embedding import Embedding
from add_norm import AddNorm
from attention import MultiHeadAttention
from forward import FeedForward

class Decoder:
    def __init__(self, outputs):
        o = Embedding(outputs)
        o = AddNorm(o, MultiHeadAttention(o))
        o = AddNorm(o, FeedForward(o))
        return o