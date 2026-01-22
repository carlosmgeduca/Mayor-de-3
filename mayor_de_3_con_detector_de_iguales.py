import streamlit as st

st.title("¿Cuál es el mayor?")
st.write("Introduce los valores para A, B y C.")

# 1. Las entradas (Inputs)
col1, col2, col3 = st.columns(3)

with col1:
    a = st.number_input("Introduce el nº A", value=0)
with col2:
    b = st.number_input("Introduce el nº B", value=0)
with col3:
    c = st.number_input("Introduce el nº C", value=0)

# 2. La lógica para decidir la LETRA
# Comparamos para ver quién gana
letra_ganadora = ""

if a > b and a > c:
    letra_ganadora = "A"
elif b > a and b > c:
    letra_ganadora = "B"
elif c > a and c > b:
    letra_ganadora = "C"
else:
    # Caso de empate (opcional, pero bueno tenerlo por si ponen números iguales)
    letra_ganadora = "Hay un empate entre los mayores"

# 3. Mostrar el resultado
st.divider()

# Aquí mostramos exactamente lo que pediste
if "empate" in letra_ganadora:
    st.header(f"{letra_ganadora}")
else:
    st.header(f"El nº mayor es: {letra_ganadora}")

# (Opcional) Texto pequeño abajo para confirmar valores
st.caption(f"Valores revisados: A={a}, B={b}, C={c}")
