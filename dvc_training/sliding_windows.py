import numpy as np
from dvc_training import config as cfg
from numpy.lib.stride_tricks import sliding_window_view
import dvc.api

#params = dvc.api.params_show()
#window_size = params["windower"]["window_size"]
window_size = 100
X = np.genfromtxt(cfg.RAW_DATA, delimiter=",", skip_header=True)

acc_x = sliding_window_view(X[:, 0], window_shape=window_size)
acc_y = sliding_window_view(X[:, 1], window_shape=window_size)

Y = np.column_stack((acc_x, acc_y))

with open(cfg.SLIDING_WINDOWS, 'wb') as f:
    np.save(f, Y)
