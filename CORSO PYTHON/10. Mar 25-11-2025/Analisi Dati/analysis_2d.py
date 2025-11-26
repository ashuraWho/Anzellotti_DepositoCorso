"""

    Modulo per l'analisi di array multidimensionali

"""

import numpy as np

class Analysis2D: # Analisi su array multidimensionali
    
    def __init__(self, data): # Args: data -> Array (1D, 2D o superiore)
        
        self.data = data
        self.original_ndim = data.ndim
        
    
    def axis_analysis(self): # Analisi per assi -> somme e medie per righe e colonne

        results = {}
        
        if self.data.ndim >= 2:
            # Analisi per array 2D+
            results['sum_columns'] = np.sum(self.data, axis=0)
            results['sum_rows'] = np.sum(self.data, axis=1)
            results['mean_columns'] = np.mean(self.data, axis=0)
            results['mean_rows'] = np.mean(self.data, axis=1)
        else:
            # Per array 1D, considera come singola riga
            results['total_sum'] = np.sum(self.data)
            results['total_mean'] = np.mean(self.data)
            print("WARNING: Axis analysis applied to 1D data")
        
        return results
        
    
    def matrix_operations(self): # Operazioni matriciali e algebriche

        results = {}
        
        # Applicabile a qualsiasi array
        results['transpose'] = np.transpose(self.data) # Trasposizione
        results['norm'] = np.linalg.norm(self.data) # Norma della matrice
        
        if self.data.ndim == 2: # Operazioni per matrici 2D
            
            # Matrice di covarianza
            if self.data.shape[0] > 1:
                results['covariance_matrix'] = np.cov(self.data.T)
            else:
                results['covariance_matrix'] = "Not computable: requires at least 2 lines"
            
            # Prodotto matriciale -> solo se quadrata
            if self.data.shape[0] == self.data.shape[1]:
                results['matrix_product'] = np.dot(self.data, self.data)
            else:
                results['matrix_product'] = "Not computable: non-square matrix"
            
            # Determinante (solo per quadrate)
            if self.data.shape[0] == self.data.shape[1]:
                try:
                    results['determinant'] = np.linalg.det(self.data)
                    
                except np.linalg.LinAlgError: # Problemi di algebra lineare 
                    results['determinant'] = "Not computable: singular matrix" # determinante = 0
            else:
                results['determinant'] = "Not computable: non-square matrix"
                    
        # Per array 3D+
        if self.data.ndim >= 3:
            results['covariance_matrix'] = "Not available for 3D+ arrays"
            results['matrix_product'] = "Not available for 3D+ arrays"
            results['determinant'] = "Not available for 3D+ arrays"
        
        return results
    
    
    def structural_analysis(self):
        return { # Dizionario
            'shape': self.data.shape,
            'number_dimensions': self.data.ndim,
            'total_size': self.data.size,
            'data_type': self.data.dtype,
            'memory': f"{self.data.nbytes} bytes"
        }
        
    
    def comprehensive_analysis(self):
        
        results = { # Dizionario
            'structural_properties': self.structural_analysis(),
            'axis_analysis': self.axis_analysis(),
            'matrix_operations': self.matrix_operations()
        }
        
        return results
    
    
    def was_original_2d(self): # Verifica se i dati originali erano 2D+
        return self.original_ndim >= 2 # True se i dati originali erano 2D+