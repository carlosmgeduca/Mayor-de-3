import streamlit as st

# Título de la aplicación
st.title("Calculadora del Número Mayor")
st.write("Introduce tres números distintos y el programa te dirá cuál es el mayor.")

# Creamos 3 columnas para que quede ordenado visualmente
col1, col2, col3 = st.columns(3)

with col1:
    a = st.number_input("Introduce el nº A", value=0)
with col2:
    b = st.number_input("Introduce el nº B", value=0)
with col3:
    c = st.number_input("Introduce el nº C", value=0)

# Lógica sencilla para calcular el mayor
# (Usamos la función max() de Python que es la forma más directa)
mayor = max(a, b, c)

# Línea divisoria visual
st.divider()

# Mostrar el resultado final destacado
# Usamos un f-string para meter la variable dentro del texto
st.header(f"El nº mayor es: {mayor}")

# Opcional: Un mensaje extra de confirmación
st.success(f"Cálculo realizado: Entre {a}, {b} y {c}, el ganador es {mayor}.")
