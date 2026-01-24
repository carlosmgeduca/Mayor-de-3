import streamlit as st

st.set_page_config(page_title="Cálculo de Entradas", layout="centered")

st.title("🎟️ Taquilla de Espectáculo")

# Entrada de datos: Precio y Cantidad
precio_unitario = st.number_input("Precio de una entrada (€):", min_value=0.0, value=50.0, step=1.0)
cantidad = st.number_input("¿Cuántas entradas deseas comprar?", value=1)

st.divider()

if st.button("Calcular Pago"):
    # Validación (Mensaje de error)
    if cantidad < 1 or cantidad > 4:
        st.error("❌ ERROR: El número de entradas debe estar entre 1 y 4.")
    else:
        # Lógica de descuentos
        descuento = 0
        if cantidad == 2:
            descuento = 0.10
        elif cantidad == 3:
            descuento = 0.15
        elif cantidad == 4:
            descuento = 0.20
        
        # Cálculos
        total_sin_dto = cantidad * precio_unitario
        ahorro = total_sin_dto * descuento
        pago_final = total_sin_dto - ahorro
        
        # Resultado simple
        st.subheader(f"Total a pagar: {pago_final:.2f} €")
        if descuento > 0:
            st.write(f"Descuento aplicado: {int(descuento*100)}%")

# Diagrama de flujo dinámico
with st.expander("Ver Diagrama de Flujo"):
    # Marcas para el diagrama
    error = " <--- (CAMINO ACTUAL)" if cantidad < 1 or cantidad > 4 else ""
    valido = " <--- (CAMINO ACTUAL)" if 1 <= cantidad <= 4 else ""
    
    st.code(f"""
          [ INICIO ]
              |
      +-------V-------+
      | Leer Precio   |
      | Leer Cantidad |
      +-------+-------+
              |
      ________V________
     /                 \\
    /  ¿Cant entre      \\
    \\  1 y 4?           /
     \\_________________/
      |               |
    ( NO )          ( SÍ )
      |               |
 [ Error ]{error}   [ Calcular Dto ]{valido}
      |               |
      |        _______V_______
      |       | ¿Cant?        |
      |       | 2 -> 10%      |
      |       | 3 -> 15%      |
      |       | 4 -> 20%      |
      |       |_______________|
      |               |
      +-------+-------+
              |
      +-------V-------+
      | Mostrar PAGO  |
      +-------+-------+
              |
           [ FIN ]
    """)
