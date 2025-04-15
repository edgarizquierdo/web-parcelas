import streamlit as st
import pandas as pd
import base64
import io

st.set_page_config(page_title="Prueba de Descarga", layout="centered")
st.title("📄 Descarga de Plantilla Excel")

# Generar la plantilla de ejemplo
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
df = pd.DataFrame(datos_ejemplo)

# Convertir el DataFrame a un archivo Excel en memoria
buffer = io.BytesIO()
df.to_excel(buffer, index=False, engine="openpyxl")
buffer.seek(0)

# Codificar el archivo Excel en base64
b64 = base64.b64encode(buffer.read()).decode()

# Crear un enlace de descarga
href = f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64}" download="plantilla_parcela.xlsx">📥 Descargar plantilla Excel</a>'

# Mostrar el enlace en la aplicación
st.markdown(href, unsafe_allow_html=True)
