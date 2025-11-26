"""

    Modulo per l'analisi di array monodimensionali

"""

import numpy as np

class Analysis1D: # Analisi statistiche su array 1D
    
    def __init__(self, data): # Args: data -> Array 1D (o che può essere convertito a 1D)
        
        self.original_data = data
        
        # Converto a 1D se necessario
        if data.ndim > 1:
            self.data = data.flatten()
        else:
            self.data = data
            
    
    def basic_statistics(self):
        return { # Dizionario
            'minimum_value': np.min(self.data),
            'maximum_value': np.max(self.data),
            'mean': np.mean(self.data),
            'standard_deviation': np.std(self.data)
        }
    
    
    def positional_analysis(self):
        return { # Dizionario
            'minimum_value_index': np.argmin(self.data),
            'index_maximum_value': np.argmax(self.data),
            'median': np.percentile(self.data, 50)
        }
        
    
    def search_analysis(self): # Analisi di ricerca e posizionamento nell'array ordinato
  
        sorted_data = np.sort(self.data) # Ordino l'array per le ricerche
        
        mean_val = np.mean(self.data)
        median_val = np.percentile(self.data, 50)
        
        return { # Dizionario
            'mean_position': np.searchsorted(sorted_data, mean_val),
            'median_position': np.searchsorted(sorted_data, median_val),
            'sorted_array': sorted_data
        }
    
    
    def comprehensive_analysis(self): # Esegue tutte le analisi 1D disponibili
   
        results = { # Dizionario
            'basic_statistics': self.basic_statistics(),
            'positional_analysis': self.positional_analysis(),
            'search_analysis': self.search_analysis()
        }
        
        return results
    
    
    def is_1d_data(self): # Verifica se i dati originali erano 1D
        return self.original_data.ndim == 1 # True se i dati originali erano 1D