import numpy as np


def inverted_dropout(x: np.ndarray, m: np.ndarray, p_keep: float) -> np.ndarray:
    x = np.asarray(x, dtype = float)
    m = np.asarray(m, dtype = int)
    out = (x * m) / p_keep
    return out
