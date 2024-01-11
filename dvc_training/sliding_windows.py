import numpy as np
import config as cfg
from numpy.lib.stride_tricks import sliding_window_view

WINDOW_SIZE = 100

X = np.genfromtxt(cfg.RAW_DATA, delimiter=",", skip_header=True)

acc_x = sliding_window_view(X[:, 0], window_shape=WINDOW_SIZE)
acc_y = sliding_window_view(X[:, 1], window_shape=WINDOW_SIZE)

Y = np.column_stack((acc_x, acc_y))

with open(cfg.SLIDING_WINDOWS, 'wb') as f:
    np.save(f, Y)
