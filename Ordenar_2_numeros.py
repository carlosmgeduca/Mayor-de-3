import streamlit as st

st.set_page_config(page_title="Lógica de Diagramas", layout="centered")

st.title("📂 Orden de Variables")
st.write("Objetivo: Determinar si el orden de salida es **A, B** o **B, A**.")

# Entrada de datos
col1, col2 = st.columns(2)
with col1:
    a = st.number_input("Valor de A:", value=0)
with col2:
    b = st.number_input("Valor de B:", value=0)

st.divider()

if st.button("EJECUTAR COMPARACIÓN"):
    # Representación visual de la decisión
    st.write(f"Evaluando condición: **¿A > B?** ({a} > {b})")
    
    if a > b:
        # Resultado basado en nombres de variables
        st.subheader("Orden: **A, B**")
        st.success("La condición fue VERDADERA (A es mayor).")
    elif b > a:
        st.subheader("Orden: **B, A**")
        st.success("La condición fue FALSA (B es mayor).")
    else:
        st.subheader("Orden: **A = B**")
        st.warning("Los valores son iguales.")

# Representación gráfica para clase
st.write("---")
st.write("### Representación en Diagrama de Flujo")



st.code(f"""
      [ INICIO ]
          |
    +-----+-----+
    | Leer A, B |
    +-----+-----+
          |
    ¿Es A > B? ---------+
      |  (SÍ)           | (NO)
      v                 v
[ Mostrar A, B ]  [ Mostrar B, A ]
      |                 |
      +-------+---------+
              |
          [ FIN ]
""")
