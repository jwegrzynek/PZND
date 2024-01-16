import numpy as np
import config as cfg
from scikit.manifold import TSNE

X = np.load(cfg.SLIDING_WINDOWS)

x_embedded = TSNE()

