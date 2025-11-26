"""

    Modulo per il caricamento e la gestione dei file di input (TXT e CSV)

"""

import numpy as np
import os # Mi serve per vedere se il file esiste o meno

class FileLoader: # Caricamento e validazione dei file di dati
    
    
    def __init__(self): # Inizializzo con dati vuoti

        self.data = None
        self.data_type = None
        self.original_shape = None
    
    
    def load_file(self, filename): # Carica un file TXT o CSV e converte in array NumPy
        
        """

            Args: filename (str) -> Percorso del file da caricare
                
            Returns: bool -> True se il caricamento è riuscito, False altrimenti
            
        """
        
        if not os.path.exists(filename): # Verifico che il file esista
            print(f"\nERROR: The file '{filename}' does not exist.")
            return False
            
        # Caricamento basato sull'estensione
        if filename.endswith('.txt'): # TXT
            self.data = np.loadtxt(filename) # Dati separati da spazi/virgole
            print("\nTXT file uploaded successfully.")
                
        elif filename.endswith('.csv'): # CSV
            self.data = np.genfromtxt(filename, delimiter=',') # Dati separati da virgole
            print("\nCSV file uploaded successfully.")
                
        else:
            print("\nUnsupported file format. Please use .txt or .csv")
            return False
            
        self.original_shape = self.data.shape # Salvo la forma originale
        self.determine_data_type() # Determino il tipo di dati
            
        print(f"\nData uploaded: {self.data.shape} | Type: {self.data_type}")
        return True
    
    
    def determine_data_type(self): # Dati 1D o 2D+ (multidimensionali)

        if self.data.ndim == 1:
            self.data_type = '1D'
        else:
            self.data_type = '2D+'
    
    
    def get_data_info(self):
        
        if self.data is None:
            return {"status": "No data loaded"}
        
        return { # Dizionario con info sui dati
            "status": "Data uploaded",
            "shape": self.data.shape,
            "type": self.data_type,
            "dtype": self.data.dtype,
            "min": np.min(self.data),
            "max": np.max(self.data),
            "mean": np.mean(self.data)
        }
    
    
    def get_data(self):
        return self.data # Array con i dati caricati
    
    
    def get_data_type(self):
        return self.data_type # str: '1D' o '2D+'