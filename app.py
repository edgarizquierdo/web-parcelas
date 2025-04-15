st.subheader("📄 Plantilla de ejemplo")
st.markdown("Descarga la plantilla base con ejemplos para rellenar correctamente los datos:")


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
