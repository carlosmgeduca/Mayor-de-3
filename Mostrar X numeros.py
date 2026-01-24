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

# Inicializamos variables para que el diagrama no de error antes de pulsar el botón
resultados = []
ejecutado = False

if st.button("Ejecutar Bucle"):
    ejecutado = True
    numero_actual = inicio
    contador = 0
    
    while contador < cantidad:
        resultados.append(str(numero_actual))
        numero_actual += salto
        contador += 1
    
    st.subheader("Resultado:")
    st.success(" , ".join(resultados))

st.divider()

# El diagrama de flujo ahora usa lógica condicional para no fallar
with st.expander("Ver Diagrama de Flujo"):
    # Si no se ha pulsado el botón, mostramos "?" en lugar de valores internos
    val_cont = cantidad if ejecutado else "?"
    res_muestra = resultados[0] if resultados else "X"

    

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
    +-----> ¿Cont < Límite? (¿Cont < {cantidad}?)
    |         |          |
    |       ( SÍ )     ( NO ) ---> [ FIN ]
    |         |
    |   +-----V-----+
    |   | MOSTRAR   | --> {res_muestra}
    |   | Cont + 1  |
    |   | Ini + Salto|
    |   +-----------+
    |         |
    +---------+
    """)
