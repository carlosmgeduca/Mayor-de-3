import streamlit as st

st.set_page_config(page_title="Bucle Dinámico Pro", layout="centered")

st.title("🔁 Generador de Sucesiones")
st.write("Configura el inicio, el salto y la cantidad de repeticiones.")

# Entradas del usuario
col1, col2, col3 = st.columns(3)
with col1:
    inicio = st.number_input("Inicio:", value=1)
with col2:
    salto = st.number_input("Incremento:", value=1)
with col3:
    cantidad = st.number_input("Nº a mostrar:", min_value=1, value=5)

if st.button("Ejecutar Bucle"):
    st.subheader("Resultado:")
    
    # Lógica del bucle
    numero_actual = inicio
    contador = 0
    resultados = []
    
    # Simulación del bucle
    while contador < cantidad:
        resultados.append(str(numero_actual))
        numero_actual += salto
        contador += 1
    
    # Mostrar los números de forma visual
    st.success(" , ".join(resultados))

# Diagrama de flujo adaptativo
with st.expander("Ver Diagrama de Flujo"):
    st.code(f"""
          [ INICIO ]
              |
      +-------V-------+
      | Inicio = {inicio}
      | Salto  = {salto}
      | Límite = {cantidad}
      | Cont   = 0
      +-------+-------+
              |
    +-----> ¿Cont < Límite? (¿{contador} < {cantidad}?)
    |         |          |
    |       ( SÍ )     ( NO ) ---> [ FIN ]
    |         |
    |   +-----V-----+
    |   | MOSTRAR   | --> {resultados[0] if resultados else "N"}
    |   | Cont + 1  |
    |   | Ini + Salto|
    |   +-----------+
    |         |
    +---------+
    """)
