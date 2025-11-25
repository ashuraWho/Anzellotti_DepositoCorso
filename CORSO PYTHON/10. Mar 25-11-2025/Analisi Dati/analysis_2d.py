"""

    Modulo per l'analisi di array multidimensionali

"""

import numpy as np

class Analysis2D: # Analisi su array multidimensionali
    
    def __init__(self, data): # Args: data -> Array 2D+
        
        self.data = data
        self.original_ndim = data.ndim
        
    
    def axis_analysis(self):
        """
        Analisi per assi - somme e medie lungo righe e colonne
        
        Returns:
            dict: Dizionario con aggregazioni per assi
        """
        results = {}
        
        if self.data.ndim >= 2:
            # Analisi per array 2D+
            results['sum_columns'] = np.sum(self.data, axis=0)
            results['sum_rows'] = np.sum(self.data, axis=1)
            results['mean_columns'] = np.mean(self.data, axis=0)
            results['mean_rows'] = np.mean(self.data, axis=1)
        