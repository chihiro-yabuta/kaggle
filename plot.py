import os, shutil
import matplotlib.pyplot as plt

def plot(x, y, dir, name):
    shutil.rmtree(dir, ignore_errors=True)
    os.makedirs(dir, exist_ok=True)
    fig = plt.figure(figsize=(20, 4), tight_layout=True)
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(x, y)
    fig.savefig(f'{dir}/{name}.pdf')
