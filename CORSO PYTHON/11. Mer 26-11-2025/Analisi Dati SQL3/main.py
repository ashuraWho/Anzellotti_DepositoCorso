import numpy as np
import os # Così se i file non esisono vado a creare i dati di esempio per i test (TXT e CSV)
import sqlite3

# Moduli progetto iniziale
from file_loader import FileLoader
from analysis_1d import Analysis1D
from analysis_2d import Analysis2D
from results_saver import ResultsSaver

# Muduli per implementazione SQL
from california_loader import load_california_csv
from sqlite_save import save_dataset_to_sqlite, save_analysis_to_sqlite
from sqlite_analysis import column_statistics

# Directory dello script
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
    
class DataAnalysisSystem: # Sistema principale -> coordina tutti i moduli
    
    def __init__(self):
        self.file_loader = FileLoader()
        self.current_results = None # Risultati dell'analisi corrente
    
    
    def run_analysis(self, analysis_type='all'): # Esegue l'analisi specificata sui dati caricati
        
        """
            Args: analysis_type (str) -> 'all', '1d' o '2d'
                
            Returns: dict -> Risultati analisi o 'None' se errore
        
        """
        
        if self.file_loader.data is None: # Vedo se non ci sono dati caricati
            print("ERROR: No data loaded. Use option (1) first.")
            return None
        
        results = {} # Dizionario per raccogliere i risultati
        data = self.file_loader.get_data() # Recupero i dati caricati
        
        # Analisi 1D -> sempre possibile (anche 2D+ -> appiattimento)
        if analysis_type in ['all', '1d']:
            
            try:
                print("\n--- 1D ANALYSIS PERFORMANCE ---")
                
                analyzer_1d = Analysis1D(data)
                results['1d_analysis'] = analyzer_1d.comprehensive_analysis()
                
                # Avviso se i dati non erano originalmente 1D
                if not analyzer_1d.is_1d_data():
                    print("\nNOTE: 1D analysis applied to multidimensional data (automatic flattening)")
                
                self.print_1d_results(results['1d_analysis']) # Stampo su schermo
                
                self.current_results = results.copy() # Salvo i risultati 1D già ora in current_results così non si perdono
                
            except Exception as e:
                print(f"\nError during 1D analysis: {e}")
                return None
            
        # Analisi 2D -> sempre possibile (anche con 1D)
        if analysis_type in ['all', '2d']:
            
            try:
                print("\n--- 2D ANALYSIS PERFORMANCE ---")
                
                analyzer_2d = Analysis2D(data)
                results['2d_analysis'] = analyzer_2d.comprehensive_analysis()
                
                # Avviso se i dati non erano originalmente 2D
                if not analyzer_2d.was_original_2d():
                    print("\nNOTE: 2D analysis applied to 1D data")
                
                self.print_2d_results(results['2d_analysis']) # Stampo su schermo
            
                # Aggiorno current_results con la parte 2D (se tutto ok)
                self.current_results = results.copy()

            except Exception as e:
                print(f"\nWarning: 2D analysis skipped due to: {e}")
                print("You can still save the 1D results (if present) or try 2D on a 2D dataset.")

        # Se almeno una analisi è stata eseguita salvo i risultati
        if results:
            self.current_results = results
            return results

        print("\nNo analysis performed.")
        return None
    
    
    def print_1d_results(self, results): # Stampa i risultati dell'analisi 1D
        
        stats = results['basic_statistics']
        pos = results['positional_analysis']
        
        print("\nBASIC STATISTICS:")
        print(f"  Minimum: {stats['minimum_value']:.4f}")
        print(f"  Maximum: {stats['maximum_value']:.4f}")
        print(f"  Mean: {stats['mean']:.4f}")
        print(f"  Standard Deviation: {stats['standard_deviation']:.4f}")
        
        print("\nPOSITIONAL ANALYSIS:")
        print(f"  Minimum value index: {pos['minimum_value_index']}")
        print(f"  Maximum value index: {pos['index_maximum_value']}")
        print(f"  Median: {pos['median']:.4f}")
    
    
    def print_2d_results(self, results): # Stampa i risultati dell'analisi 2D

        structural = results['structural_properties']
        axis = results['axis_analysis']
        matrix = results['matrix_operations']
        
        print("\nSTRUCTURAL PROPERTIES:")
        print(f"  Shape: {structural['shape']}")
        print(f"  Dimensions: {structural['number_dimensions']}")
        print(f"  Total elements: {structural['total_size']}")
        print(f"  Memory usage: {structural['memory']}")
        
        print("\nAXIS ANALYSIS:")
        for key, value in axis.items():
            if isinstance(value, np.ndarray):
                print(f"  {key}: array shape {value.shape}") # Per array stampo solo la forma
            else:
                print(f"  {key}: {value:.4f}") # Per valori numerici stampo con 4 decimali
        
        print("\nMATRICIAL OPERATIONS:")
        for key, value in matrix.items():
            if key == 'norm':
                print(f"  {key}: {value:.4f}") # Norma con 4 decimali
            elif isinstance(value, np.ndarray):
                print(f"  {key}: array shape {value.shape}") # Stampo forma array
            else:
                print(f"  {key}: {value}") # Gli altri valori li stampo normali
    
    
    def save_current_results(self, filename, format_type='txt'): # Salva i risultati correnti in file
        
        """
        
            Args:
                1. filename (str): Nome del file
                2. format_type (str): 'txt' o 'csv'
                
        """
        
        if self.current_results is None:
            print("\nThere are no results to save. Please run an analysis first.")
            return False
        
        saver = ResultsSaver(self.current_results) # Salvo i risultati
        return saver.save_analysis(filename, format_type)



def main():

    system = DataAnalysisSystem()
    
    while True:
        
        print("\n--- DATA ANALYSIS SYSTEM ---")
        print("(1) Upload file (TXT/CSV)")
        print("(2) Full analysis (1D + 2D)")
        print("(3) 1D analysis only")
        print("(4) 2D analysis only")
        print("(5) Save results")
        print("(6) Data information")
        print("(7) Import California CSV")
        print("(8) Save cleaned dataset to SQLite DB (DB1)")
        print("(9) Save analysis results to SQLite DB (DB2)")
        print("(0) Exit")
        
        scelta = input("\nChoose an option (0-9): ").strip()
        
        match scelta:
            
            case "1": # Caricamento file
                
                filename = input("\nEnter the file path: ").strip()
                if system.file_loader.load_file(filename):
                    print("\nFile uploaded successfully!")
                    system.current_results = None
                else:
                    print("\nError uploading file")
            
            case "2": # Analisi completa
                system.run_analysis('all')
            
            case "3": # Solo analisi 1D
                system.run_analysis('1d')
            
            case "4": # Solo analisi 2D
                system.run_analysis('2d')
            
            case "5": # Salvataggio risultati
                
                if system.current_results is not None:
                    output_name = input("Output file name (without extension): ").strip()
                    format_choice = input("Format (TXT/CSV) [default: TXT]: ").strip().lower()
                    
                    if format_choice not in ['txt', 'csv']:
                        format_choice = 'txt'
                    
                    filename = f"{output_name}.{format_choice}"
                    file_path = os.path.join(CURRENT_DIR, filename)
                    if system.save_current_results(file_path, format_choice):
                        print("\nResults saved successfully!")
                    else:
                        print("\nError saving")
                else:
                    print("\nNo results to save")
            
            case "6": # Informazioni dati
                
                info = system.file_loader.get_data_info()
                print("\nCURRENT DATA INFORMATION:")
                for key, value in info.items():
                    print(f"  {key}: {value}")
                    
            case "7": # Import California CSV
                
                csv_path = input("\nPath to California CSV (or press 'Enter' to use 'example.csv'): ").strip()
                if not csv_path:
                    csv_path = os.path.join(CURRENT_DIR, 'example.csv')
                
                try:
                    data_arr, colnames = load_california_csv(csv_path, delimiter=',', has_header=True) # Mi restituisce (clean_array, column_names)
                    
                    # Carico i dati dentro FileLoader
                    system.file_loader.data = data_arr
                    system.file_loader.original_shape = data_arr.shape
                    system.file_loader.determine_data_type()
                    
                    # Setto il tipo in base alla ndim
                    system.file_loader.data_type = '2D+' if data_arr.ndim >= 2 else '1D'
                    print(f"\nLoaded California dataset: shape={data_arr.shape}, columns={colnames}")
                    
                    system.current_results = None
                except Exception as e:
                    print(f"\nError loading California CSV: {e}")
                    
            case "8": # Salvo il dataset pulito nel DB1
                
                if system.file_loader.data is None :
                    print("\nNo data loaded. Use option (1) or (7) first.")
                
                else:
                    dbname = input("\nDB file name [default: housing_clean.db]: ").strip() or "housing_clean.db"
                    table = input("Table name [default: housing]: ").strip() or "housing"
                    
                    # Uso i nomi colonne di default -> se non ho match li creo generici
                    colnames = ["MedInc","HouseAge","AveRooms","AveBedrms","Population","AveOccup","Latitude","Longitude","MedHouseVal"]
                    if system.file_loader.data.shape[1] != len(colnames):
                        colnames = [f"col{idx}" for idx in range(system.file_loader.data.shape[1])]
                    
                    dbpath = os.path.join(CURRENT_DIR, dbname)
                    
                    ok = save_dataset_to_sqlite(dbpath, table, system.file_loader.data, colnames)
                    if ok:
                        print(f"\nDataset saved to {dbpath} table {table}")
                    
            case "9": # Salvo i risultati dell'analisi nel DB2 -> non mi torna la stampa del DB2 (devo vederla)
                
                if system.current_results is None:
                    print("\nNo analysis results present. Run analysis first.")
                else:
                    dbname = input("\nDB file name for analysis [default: housing_analysis.db]: ").strip() or "housing_analysis.db"
                    table = input("Table name [default: stats]: ").strip() or "stats"
                    
                    try: # Se ho dataset 2D -> calcolo stats per colonna (per 'interpretation')
                        if system.file_loader.data is not None and system.file_loader.data.ndim == 2:
                            colnames = ["MedInc","HouseAge","AveRooms","AveBedrms","Population","AveOccup","Latitude","Longitude","MedHouseVal"]
                            
                            if system.file_loader.data.shape[1] != len(colnames):
                                colnames = [f"col{idx}" for idx in range(system.file_loader.data.shape[1])]
                                
                            col_stats = column_statistics(system.file_loader.data, colnames)
                            dbpath = os.path.join(CURRENT_DIR, dbname)
                            
                            save_analysis_to_sqlite(dbpath, table, system.current_results) # Salvo la struttura base dei risultati
                            
                            # Apro il DB per aggiungere le righe con le interpretazioni per ogni colonna
                            conn = sqlite3.connect(dbpath)
                            cur = conn.cursor()
                            
                            for s in col_stats: # Inserisco cinque righe per ogni colonna: min/max/mean/median/std con interpretation
                                cur.execute(f"INSERT INTO {table} (variable, stat, value, interpretation) VALUES (?, ?, ?, ?)",
                                            (s['variable'], 'min', str(s['min']), s['interpretation']))
                                cur.execute(f"INSERT INTO {table} (variable, stat, value, interpretation) VALUES (?, ?, ?, ?)",
                                            (s['variable'], 'max', str(s['max']), s['interpretation']))
                                cur.execute(f"INSERT INTO {table} (variable, stat, value, interpretation) VALUES (?, ?, ?, ?)",
                                            (s['variable'], 'mean', str(s['mean']), s['interpretation']))
                                cur.execute(f"INSERT INTO {table} (variable, stat, value, interpretation) VALUES (?, ?, ?, ?)",
                                            (s['variable'], 'median', str(s['median']), s['interpretation']))
                                cur.execute(f"INSERT INTO {table} (variable, stat, value, interpretation) VALUES (?, ?, ?, ?)",
                                            (s['variable'], 'std', str(s['std']), s['interpretation']))
                                
                            conn.commit()
                            conn.close()
                            print(f"\nAnalysis results and column statistics saved to {dbpath} table {table}")
                            
                        else: # Senza dataset completo salvo solo i risultati aggregati
                                dbpath = os.path.join(CURRENT_DIR, dbname)
                                save_analysis_to_sqlite(dbpath, table, system.current_results)
                                print(f"\nAnalysis results saved to {dbpath} table {table}")
                                
                    except Exception as e:
                        print(f"\nError saving analysis to DB: {e}")
     
            case "0": # Uscita
                
                print("\nExit.")
                break
            
            case _: # Sintassi non valida
                print("\nInvalid option. Choose between 0 and 9.")


if __name__ == "__main__":
    
    # Percorsi completi
    txt_path = os.path.join(CURRENT_DIR, 'example.txt')
    csv_path = os.path.join(CURRENT_DIR, 'example.csv')

    # Creo dati di esempio per i test (TXT e CSV)
    if not os.path.exists(txt_path):
        np.savetxt(txt_path, np.random.rand(10))
        print(f"Created sample file: {txt_path}")

    # Crea example.csv se non esiste
    if not os.path.exists(csv_path):
        np.savetxt(csv_path, np.random.rand(5, 4), delimiter=',')
        print(f"Created sample file: {csv_path}")
    
    # Avvio il sistema
    main()