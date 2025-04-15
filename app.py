import streamlit as st
import pandas as pd
import io
import base64
from importar_parcelas import importar_parcelas

st.set_page_config(page_title="Gestión de parcelas", layout="centered")
st.title("🌾 Aplicación de carga y validación de parcelas agrícolas")

st.markdown("Bienvenido. Puedes **descargar la plantilla**, rellenarla y luego **subir tu archivo Excel** para validarlo.")

# 🔹 SECCIÓN 1: DESCARGAR PLANTILLA
st.header("📄 Descargar plantilla de ejemplo")

def generar_excel():
    datos = {
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
    df = pd.DataFrame(datos)
    buffer = io.BytesIO()
    df.to_excel(buffer, index=False, engine="openpyxl")
    buffer.seek(0)
    return buffer.read()

excel_data = generar_excel()
b64_excel = base64.b64encode(excel_data).decode()
link_descarga = f'<a href="data:application/octet-stream;base64,{b64_excel}" download="plantilla_parcela.xlsx">📥 Haz clic aquí para descargar la plantilla</a>'
st.markdown(link_descarga, unsafe_allow_html=True)

# 🔹 SECCIÓN 2: SUBIR Y VALIDAR ARCHIVO
st.header("🧾 Subir y validar tu archivo Excel")

archivo = st.file_uploader("Selecciona el archivo Excel con tus parcelas", type=["xlsx"])

if archivo is not None:
    with open("archivo_temporal.xlsx", "wb") as f:
        f.write(archivo.read())

    df_validas, df_errores = importar_parcelas("archivo_temporal.xlsx")

    if df_validas is not None:
        st.success(f"✅ {len(df_validas)} fila(s) válidas encontradas.")
        st.dataframe(df_validas)

        buffer_validas = io.BytesIO()
        df_validas.to_excel(buffer_validas, index=False, engine="openpyxl")
        st.download_button("📥 Descargar datos válidos", buffer_validas.getvalue(), "datos_validos.xlsx")

        if not df_errores.empty:
            st.warning(f"⚠️ {len(df_errores)} fila(s) con errores.")
            st.dataframe(df_errores)

            buffer_errores = io.BytesIO()
            df_errores.to_excel(buffer_errores, index=False, engine="openpyxl")
            st.download_button("📥 Descargar filas con errores", buffer_errores.getvalue(), "datos_con_errores.xlsx")
        else:
            st.info("🎉 No se detectaron errores en los datos.")
    else:
        st.error("❌ No se ha podido procesar el archivo.")
