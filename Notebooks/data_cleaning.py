def remove_duplicates(df):
    return df.drop_duplicates()

def fill_nulls(df):
    return df.fillna(method='ffill')

def estandarizar_columnas(df):     
    nuevos_nombres = {}
    for col in df.columns:       
        nombre_limpio = col.lower()        
        nombre_limpio = nombre_limpio.replace(' ', '_').replace('-', '_')
        nombre_limpio = nombre_limpio.replace('(', '').replace(')', '') 
        nombre_limpio = nombre_limpio.replace('.', '').replace('/', '_')
        nuevos_nombres[col] = nombre_limpio        
    return df.rename(columns=nuevos_nombres)


