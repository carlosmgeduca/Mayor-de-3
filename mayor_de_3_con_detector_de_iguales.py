import streamlit as st

def main():
    st.title("🔍 Encuentra el Mayor (Lógica Estricta)")
    st.write("Introduce 3 números. El sistema fallará si hay empate en los mayores.")

    # 1. Entradas (Inputs) en la web
    col1, col2, col3 = st.columns(3)
    
    with col1:
        A = st.number_input("Número A", value=0, step=1.0)
    with col2:
        B = st.number_input("Número B", value=0, step=1.0)
    with col3:
        C = st.number_input("Número C", value=0, step=1.0)

    # Botón para ejecutar
    if st.button("Calcular cuál es mayor"):
        
        # 2. La lógica (idéntica a la anterior)
        if A > B and A > C:
            st.success(f"✅ El mayor es A: {A}")
            st.balloons()
            
        elif B > A and B > C:
            st.success(f"✅ El mayor es B: {B}")
            st.balloons()
            
        elif C > A and C > B:
            st.success(f"✅ El mayor es C: {C}")
            st.balloons()
            
        else:
            # 3. El error visual
            st.error("❌ Error: No se puede determinar un único mayor (hay números iguales).")

if __name__ == "__main__":
    main()
