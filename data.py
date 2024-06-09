import torch

def data(mi, ma, step):
    x = torch.arange(mi, ma, step)
    y = torch.sin(x)
    return x, y