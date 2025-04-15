import streamlit as st
from importar_parcelas import importar_parcelas
import io
import pandas as pd

st.set_page_config(page_title="Carga de parcelas agrícolas", layout="centered")
st.title("🌾 Carga de datos de parcelas agrícolas")

st.markdown("""
Sube un archivo Excel (.xlsx) con los datos de tus parcelas. El formato debe contener estas columnas obligatorias:

- nombre de parcela  
- código sigpac  
- municipio  
- superficie  
- cultivo  
- variedad  
- año de plantación  
- tipo de manejo hídrico  
- tipo de cultivo
""")

# Botón para descargar la plantilla
st.subheader("📄 Plantilla de ejemplo")
st.markdown("Descarga la plantilla base con ejemplos para rellenar correctamente los datos:")

@st.cache_data
def generar_plantilla():
    datos_ejemplo = {
        "nombre de parcela": ["Parcela 1", "Parcela 2"],
        "código sigpac": ["123456789ABC", "987654321XYZ"],
        "municipio": ["Olite", "Vilafranca del Penedès"],
        "superficie": [1.5, 2.3],
        "cultivo": ["Olivo", "Vid"],
        "variedad": ["Picual", "Tempranillo"],
        "año de plantación": [2005, 2010],
        "tipo de manejo hídrico": ["secano", "regadío"],
        "tipo de cultivo": ["ecológico", "biodinámico"]
    }
    df_ejemplo = pd.DataFrame(datos_ejemplo)
    buffer = io.BytesIO()
    df_ejemplo.to_excel(buffer, index=False, engine="openpyxl")
    return buffer.getvalue()

st.download_button(
    label="📥 Descargar plantilla Excel",
    data=generar_plantilla(),
    file_name="plantilla_parcela.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)

archivo = st.file_uploader("Selecciona el archivo Excel", type=["xlsx"])

if archivo is not None:
    ruta_temporal = "archivo_temporal.xlsx"
    with open(ruta_temporal, "wb") as f:
        f.write(archivo.read())

    df_validas, df_errores = importar_parcelas(ruta_temporal)

    if df_validas is not None:
        st.success(f"✅ Se han cargado {len(df_validas)} fila(s) válidas correctamente.")
        st.dataframe(df_validas)

        buffer_validas = io.BytesIO()
        df_validas.to_excel(buffer_validas, index=False, engine="openpyxl")
        st.download_button(
            "📥 Descargar datos válidos",
            data=buffer_validas.getvalue(),
            file_name="parcelas_validas.xlsx",
            mime="application/vnd.openxmlformats
