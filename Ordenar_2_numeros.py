import streamlit as st

st.set_page_config(page_title="Lógica de Diagramas", layout="centered")

st.title("🔢 Ordenar Variables")

# Entrada de datos
col1, col2 = st.columns(2)
with col1:
    a = st.number_input("Valor de A:", value=0)
with col2:
    b = st.number_input("Valor de B:", value=0)

if st.button("Comparar"):
    if a > b:
        st.subheader("Orden: A, B")
    elif b > a:
        st.subheader("Orden: B, A")
    else:
        st.subheader("Orden: A = B")

# Diagrama oculto y dinámico
with st.expander("Ver Diagrama de Flujo"):
    # Marcamos con una flecha el camino que está tomando el programa
    camino_si = " <--- (CAMINO ACTUAL)" if a > b else ""
    camino_no = " <--- (CAMINO ACTUAL)" if b > a else ""
    
    st.code(f"""
      [ INICIO ]
          |
    +-----+-----+
    | Leer A, B |
    +-----+-----+
          |
    ¿Es A > B?
      |         |
     (SÍ)      (NO)
      |         |
      V         V
   [A, B]{camino_si}    [B, A]{camino_no}
      |         |
      +----+----+
           |
        [ FIN ]
    """)
