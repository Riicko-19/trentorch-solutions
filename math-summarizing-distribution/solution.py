import numpy as np


def skewness(x: np.ndarray) -> float:
    mean = np.mean(x)
    std = np.std(x)
    if std == 0:
        return 0.0
    
    skew = np.mean(((x - mean) / std)**3)
    return float(skew)


def summarize_distribution(x: np.ndarray) -> dict:
    mean = np.mean(x)
    median = np.median(x)
    skew = skewness(x)
    std = np.std(x)
    
    return {
        "mean": float(mean),
        "median": float(median),
        "skew": skew,
        "std": float(std)
    }
