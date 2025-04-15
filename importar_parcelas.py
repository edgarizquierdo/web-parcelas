import pandas as pd
import os

def importar_parcelas(ruta_excel):
    """
    Carga y valida un archivo Excel con información de parcelas agrícolas.
    Devuelve dos DataFrames: uno con datos válidos y otro con errores.
    """
    if not os.path.exists(ruta_excel):
        raise FileNotFoundError("No se encuentra el archivo especificado.")

    try:
        df_original = pd.read_excel(ruta_excel)
        columnas_obligatorias = [
            "nombre de parcela",
            "código sigpac",
            "municipio",
            "superficie",
            "cultivo",
            "variedad",
            "año de plantación",
            "tipo de manejo hídrico",
            "tipo de cultivo"
        ]

        # Verificar columnas
        faltantes = [col for col in columnas_obligatorias if col not in df_original.columns]
        if faltantes:
            raise ValueError(f"Faltan las siguientes columnas en el Excel: {', '.join(faltantes)}")

        df = df_original.copy()
        df["año de plantación"] = pd.to_numeric(df["año de plantación"], errors="coerce")
        df["superficie"] = pd.to_numeric(df["superficie"], errors="coerce")

        df_validas = df[
            (df["superficie"] > 0) &
            (df["año de plantación"].notna()) &
            (df["año de plantación"] > 0)
        ]

        df_errores = df[~df.index.isin(df_validas.index)]

        return df_validas, df_errores

    except Exception as e:
        print(f"Error al importar el archivo: {e}")
        return None, None
