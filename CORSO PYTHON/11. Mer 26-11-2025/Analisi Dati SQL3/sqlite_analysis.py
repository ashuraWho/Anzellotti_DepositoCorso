import numpy as np

def column_statistics(data: np.ndarray, column_names):

    stats = []
    ncols = data.shape[1]
    
    for j in range(ncols):
        
        col = data[:, j].astype(float)
        min = float(np.min(col))
        max = float(np.max(col))
        mean = float(np.mean(col))
        median = float(np.percentile(col, 50))
        std = float(np.std(col))
        interpretation = interpret_column(col, min, max, mean, median, std)
        
        stats.append({
            'variable': column_names[j],
            'min': min,
            'max': max,
            'mean': mean,
            'median': median,
            'std': std,
            'interpretation': interpretation
        })
        
    return stats

def interpret_column(col: np.ndarray, mn: float, mx: float, mean: float, med: float, std: float):
    
    """
    
    Interpretazioni:
        - rel_std = std/|mean| -> per valutare variazione relativa
        - mean vs median -> per asimmetria
    
    """
    
    s = "" # Stringa da riempire
    
    if mean != 0:
        rel_std = std / abs(mean)
    else:
        rel_std = float('inf')

    # std/|mean|
    if rel_std > 0.5:
        s += "High variability across records. "
    elif rel_std < 0.1:
        s += "Low variability across records (values clustered around the mean). "
    else:
        s += "Moderate variability across records. "

    # mean vs median -> "distorsione"
    if mean > med:
        s += "Distribution is right-skewed (mean > median). "
    elif mean < med:
        s += "Distribution is left-skewed (mean < median). "
    else:
        s += "Distribution approximately symmetric (mean = median). "

    return s