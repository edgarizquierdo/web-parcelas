import streamlit as st
import pandas as pd
import io

st.set_page_config(page_title="Prueba plantilla", layout="centered")
st.title("🧪 Prueba del botón de plantilla Excel")

st.subheader("📄 Plantilla de ejemplo")
st.markdown("Haz clic en el botón para descargar el archivo Excel con datos de muestra.")

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
    df = pd.DataFrame(datos_ejemplo)
    buffer = io.BytesIO()
    df.to_excel(buffer, index=False, engine="openpyxl")
    return buffer.getvalue()

st.download_button(
    label="📥 Descargar plantilla Excel",
    data=generar_plantilla(),
    file_name="plantilla_parcela.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)
