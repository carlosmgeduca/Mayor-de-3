import streamlit as st

st.title("Comparador: A vs B")
st.write("Introduce los valores para ver cuál es mayor.")

# 1. Las entradas (Inputs) - Usamos 2 columnas en lugar de 3
col1, col2 = st.columns(2)

with col1:
    a = st.number_input("Introduce el nº A", value=0)
with col2:
    b = st.number_input("Introduce el nº B", value=0)

# 2. La lógica para decidir quién gana
# Aquí es muy simple: o gana A, o gana B, o son iguales.
if a > b:
    mensaje = "El nº mayor es: A"
elif b > a:
    mensaje = "El nº mayor es: B"
else:
    mensaje = "Son iguales (Empate)"

# 3. Mostrar el resultado
st.divider()
st.header(mensaje)

# (Opcional) Texto pequeño para confirmar
st.caption(f"Comparando: A={a} contra B={b}")
