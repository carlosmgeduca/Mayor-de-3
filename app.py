import streamlit as st
import graphviz

# 1. Título y explicación
st.title("Diagrama de Flujo: El Mayor de 3 Números")
st.markdown("Introduce tres valores y observa cómo cambia el flujo de decisión.")

# 2. Entradas del usuario (Inputs)
col1, col2, col3 = st.columns(3)
with col1:
    a = st.number_input("Valor A", value=0)
with col2:
    b = st.number_input("Valor B", value=0)
with col3:
    c = st.number_input("Valor C", value=0)

# 3. Lógica para determinar el mayor y el color del camino
# Colores por defecto (negro)
color_a_b = "black"
color_a_c = "black"
color_b_c = "black"
color_res_a = "black"
color_res_b = "black"
color_res_c = "black"

# Lógica
mayor = 0
resultado_texto = ""

if a > b:
    color_a_b = "green" # A es mayor que B
    if a > c:
        color_a_c = "green" # A es mayor que C
        mayor = a
        resultado_texto = "A es el mayor"
        color_res_a = "green"
    else:
        color_a_c = "red" # A no es mayor que C
        mayor = c
        resultado_texto = "C es el mayor"
        color_res_c = "green"
else:
    color_a_b = "red" # A no es mayor que B
    if b > c:
        color_b_c = "green"
        mayor = b
        resultado_texto = "B es el mayor"
        color_res_b = "green"
    else:
        color_b_c = "red"
        mayor = c
        resultado_texto = "C es el mayor"
        color_res_c = "green"

# 4. Mostrar el resultado escrito
st.success(f"Resultado: {resultado_texto} ({mayor})")

# 5. Dibujar el Diagrama
# Usamos Graphviz para pintar el diagrama
dot = graphviz.Digraph()

# Nodos (Cajitas)
dot.node('Start', 'Inicio', shape='oval')
dot.node('Dec1', '¿Es A > B?', shape='diamond')
dot.node('Dec2', '¿Es A > C?', shape='diamond')
dot.node('Dec3', '¿Es B > C?', shape='diamond')

dot.node('ResA', 'A es Mayor', shape='box', style='filled', color='lightgrey')
if color_res_a == "green": dot.node('ResA', 'A es Mayor', shape='box', style='filled', color='lightgreen')

dot.node('ResB', 'B es Mayor', shape='box', style='filled', color='lightgrey')
if color_res_b == "green": dot.node('ResB', 'B es Mayor', shape='box', style='filled', color='lightgreen')

dot.node('ResC', 'C es Mayor', shape='box', style='filled', color='lightgrey')
if color_res_c == "green": dot.node('ResC', 'C es Mayor', shape='box', style='filled', color='lightgreen')

# Conexiones (Flechas)
dot.edge('Start', 'Dec1')

# A > B
dot.edge('Dec1', 'Dec2', label='Sí', color=color_a_b, penwidth='2.0' if color_a_b=='green' else '1.0')
dot.edge('Dec1', 'Dec3', label='No', color='green' if color_a_b=='red' else 'black', penwidth='2.0' if color_a_b=='red' else '1.0')

# A > C
dot.edge('Dec2', 'ResA', label='Sí', color=color_a_c, penwidth='2.0' if color_a_c=='green' else '1.0')
dot.edge('Dec2', 'ResC', label='No', color='green' if color_a_c=='red' else 'black', penwidth='2.0' if color_a_c=='red' else '1.0')

# B > C
dot.edge('Dec3', 'ResB', label='Sí', color=color_b_c, penwidth='2.0' if color_b_c=='green' else '1.0')
dot.edge('Dec3', 'ResC', label='No', color='green' if color_b_c=='red' else 'black', penwidth='2.0' if color_b_c=='red' else '1.0')

# Mostrar diagrama en la web
st.graphviz_chart(dot)