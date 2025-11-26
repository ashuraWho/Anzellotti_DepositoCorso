import sqlite3
import os
import numpy as np

def ensure_dir_for_file(path: str): # Crea la directory se non esiste
    directory = os.path.dirname(path)
    
    if directory and not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)


def save_dataset_to_sqlite(db_path: str, table_name: str, data: np.ndarray, column_names):
    
    """
    
        Salva il dataset in una tabella SQLite:
            - tutti i campi (tranne id) sono real
            - crea la tabella se non esiste e inserisce tutte le righe
    
    """
    
    ensure_dir_for_file(db_path)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Costruzione della query CREATE TABLE
    cols_defs = ", ".join([f"'{cn}' REAL" for cn in column_names])
    create_sql = f"CREATE TABLE IF NOT EXISTS {table_name} (id INTEGER PRIMARY KEY AUTOINCREMENT, {cols_defs});"
    cursor.execute(create_sql)

    # Preparazione INSERT
    placeholders = ", ".join(["?"] * len(column_names))
    insert_sql = f"INSERT INTO {table_name} ({', '.join(['`'+cn+'`' for cn in column_names])}) VALUES ({placeholders})"
    
    # Convertiamo ogni riga in tuple di float
    rows = [tuple(map(float, row)) for row in data]
    cursor.executemany(insert_sql, rows)
    
    conn.commit()
    conn.close()
    
    return True


def flatten_analysis_results(results): # Tasformara la struttura results in righe che poi vengono inserite nella tabella stats

    rows = []
    
    # 1D basic statistics flatterate
    if '1d_analysis' in results:
        basic = results['1d_analysis'].get('basic_statistics', {})
        pos = results['1d_analysis'].get('positional_analysis', {})
        varname = "_1d_all"
        
        for key, value in basic.items():
            rows.append({"variable": varname, "stat": key, "value": float(value)})
            
        for key, value in pos.items():
            rows.append({"variable": varname, "stat": key, "value": float(value)})
            
    # 2D arrays
    if '2d_analysis' in results:
        struct = results['2d_analysis'].get('structural_properties', {})
        axis = results['2d_analysis'].get('axis_analysis', {})
        
        for key, value in struct.items():
            rows.append({"variable": "_2d_structure", "stat": key, "value": str(value)})
            
        for aname, aval in axis.items():
            if isinstance(aval, np.ndarray):
                for idx, val in enumerate(aval):
                    rows.append({"variable": f"{aname}.col{idx}", "stat": "value", "value": float(val)})
                    
            else:
                rows.append({"variable": f"{aname}", "stat": "value", "value": float(aval)})
                
    return rows


def save_analysis_to_sqlite(db_path: str, table_name: str, results):
    
    """
    
        Salva i risultati dell'analisi in una tabella:
            id, variable, stat, value, interpretation
            
        'interpretation' è lasciato vuoto se non viene fornito
        
    """
    
    ensure_dir_for_file(db_path)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    create_sql = f"""
    CREATE TABLE IF NOT EXISTS {table_name} (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        variable TEXT,
        stat TEXT,
        value TEXT,
        interpretation TEXT
    );
    """
    
    cursor.execute(create_sql)

    # Appiattisco i risultati e li inserisco
    rows = list(flatten_analysis_results(results))
    insert_sql = f"INSERT INTO {table_name} (variable, stat, value, interpretation) VALUES (?, ?, ?, ?)"
    to_insert = [(r["variable"], r["stat"], str(r["value"]), "") for r in rows]
    if to_insert:
        cursor.executemany(insert_sql, to_insert)
        
    conn.commit()
    conn.close()
    
    return True