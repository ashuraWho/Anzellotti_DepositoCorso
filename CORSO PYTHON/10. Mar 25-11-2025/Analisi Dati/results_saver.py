"""

    Modulo per il salvataggio dei risultati in TXT e CSV

"""

import numpy as np

class ResultsSaver: # Classe per salvare i risultati
    
    def __init__(self, results): # Args: results -> Dizionario con i risultati
        self.results = results
    
    # ------------------------------------------------------

    def save_txt(self, file_path): # Salva i risultati in formato TXT
        
        """
        
            Args: file_path (str) -> Path del file output
                
            Returns: bool -> True se il salvataggio è riuscito
        
        """
        
        try:
            with open(file_path, 'w') as f:
                
                # Intestazione
                f.write("# DATA ANALYSIS RESULTS\n\n") # Metto il '#' all'inizio almeno se poi viene in lettura questa roba è commentata
                
                # Scrivo i risultati per ogni tipo di analisi
                for analysis_type, analysis_data in self.results.items():
                    f.write(f"# {analysis_type.upper()}\n") # Scrivo il titolo dell'analisi, p.e. ANALISI_1D
                    
                    if isinstance(analysis_data, dict): # Se è un dizionario uso la funzione ricorsiva (visto ad astrofisica)
                        self.write_dict_recursive(f, analysis_data, indent=2)
                        
                    else: # Se è un valore semplice lo scrivo direttamente
                        f.write(f"  {analysis_data}\n")
                    
                    f.write("\n") # Per separare le sezioni
            
            print(f"\nResults saved in TXT format: {file_path}")
            return True
            
        except Exception as e:
            print(f"\nError saving TXT: {e}")
            return False
    
    # FUNZIONE RICORSIVA PER TXT
    def write_dict_recursive(self, file_obj, data_dict, indent=0): # Scrive ricorsivamente un dizionario nel file
        
        """
        
            Args:
                1. file_obj -> File object aperto
                2. data_dict (dict) -> Dizionario da scrivere
                3. indent (int) -> Livello di indentazione
            
        """
        
        indent_str = " " * indent # Indentazione
        
        for key, value in data_dict.items(): # Itero su tutte le coppie chiave-valore del dizionario
            
            # --- Caso ricorsivo -> 'value' è un dizionario annidato ---
            # CASO 1: il valore è un sottodizionario
            if isinstance(value, dict):
                # Scrivo la chiave e poi ricorro sul sottodizionario
                file_obj.write(f"{indent_str}{key}:\n")
                self.write_dict_recursive(file_obj, value, indent + 2) # Chiamo ricorsivamente -> aumento l'indentazione 
            
            # CASO 2: il valore è un array
            elif isinstance(value, np.ndarray):
                # Converto l'array in lista
                array_list = value.tolist()
                
                # Controllo lunghezza
                if len(str(array_list)) > 100: # Se troppo lungo tronco con le info base
                    file_obj.write(f"{indent_str}{key}: [array di {len(array_list)} elementi]\n")
                else: # Stampo tutta la lista
                    file_obj.write(f"{indent_str}{key}: {array_list}\n")
            
            # CASO 3: Valore semplice (numero, stringa, booleano -> non dict) 
            else:
                # --- Caso base -> ferma la ricorsione (condizione di uscita) ---
                file_obj.write(f"{indent_str}{key}: {value}\n") # Scrivo la coppia chiave-valore
    
    # ------------------------------------------------------
    
    def save_csv(self, file_path): # Salva i risultati in formato CSV
        
        """
        
            Args: file_path (str) -> Path del file di output
                
            Returns: bool -> True se il salvataggio è riuscito
        
        """
        
        try:
            with open(file_path, 'w') as f:
                
                f.write("# analysis_type, category, parameter, value\n") # Intestazione colonne CSV
                
                # Scrivo ogni risultato come riga CSV
                for analysis_type, analysis_data in self.results.items(): # Ciclo per tutti i risultati
                    self.flatten_dict_to_csv(f, analysis_type, analysis_data) # Appiattisco il dizionario in righe CSV
            
            print(f"\nResults saved in CSV format: {file_path}")
            return True
            
        except Exception as e:
            print(f"\nError saving CSV: {e}")
            return False
    
    
    # FUNZIONE RICORSIVA PER SCV
    def flatten_dict_to_csv(self, file_obj, analysis_type, data_dict, category=""): # Appiattisce ricorsivamente il dizionario in righe CSV
        
        """
        
            Args:
                1. file_obj: File object aperto
                2. analysis_type (str): Tipo di analisi
                3. data_dict (dict): Dizionario da appiattire
                4. category (str): Categoria corrente
        
        """
        
        for key, value in data_dict.items():
            if category: # Se 'category' esiste -> "statistiche_base.valore_minimo"
                current_category = f"{category}.{key}"
            else: # Se 'category' è vuota -> "statistiche_base"
                current_category = key
            
            # CASO 1: Valore è un sottodizionario
            if isinstance(value, dict):
                self.flatten_dict_to_csv(file_obj, analysis_type, value, current_category) # Ricorsione -> nuova categoria
            
            # CASO 2: Valore è un array
            elif isinstance(value, np.ndarray):
                # Converto in lista e tronco se troppo lunga
                array_repr = str(value.tolist())[:100] # Massimo 100 caratteri
                file_obj.write(f"{analysis_type},{current_category},array,{array_repr}\n")
                
            # CASO 3: Valore semplice
            else:
                file_obj.write(f"{analysis_type},{current_category},{key},{value}\n")
    
    # ------------------------------------------------------
    
    def save_analysis(self, file_path, format_type='txt'): # Metodo per salvare nei diversi formati
        
        """
        
            Args:
                1. file_path (str): Nome del file di output
                2. format_type (str): 'txt' o 'csv'
                
            Returns: bool -> True se il salvataggio è riuscito
        
        """
        
        if format_type.lower() == 'txt':
            return self.save_txt(file_path)
        
        elif format_type.lower() == 'csv':
            return self.save_csv(file_path)
        
        else:
            print(f"Unsupported format: {format_type}")
            return False