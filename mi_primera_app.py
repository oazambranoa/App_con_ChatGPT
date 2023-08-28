import streamlit as st

# Título y autor
st.title("Mi primera app")
st.write("Autor: Esta app fue elaborada por Omar Zambrano.")

# Preguntar el nombre al usuario
nombre_usuario = st.text_input("Por favor, ingresa tu nombre")

# Imprimir el mensaje de bienvenida
if nombre_usuario:
    mensaje = f"{nombre_usuario}, te doy la bienvenida a mi primera app."
    st.write(mensaje)
