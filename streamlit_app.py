import streamlit as st
import openai

# Función para generar texto utilizando GPT-3
def generate_text(prompt, api_key):
    openai.api_key = api_key
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7
    )
    return response.choices[0].text.strip()

# Función para la página de inicio
def home():
    st.title("Fashion App")
    st.write("Bienvenido a la aplicación Fashion")

# Función para mostrar las últimas tendencias de moda
def latest_trends(api_key):
    st.title("Últimas tendencias de moda")
    st.write("Aquí puedes encontrar las últimas tendencias de moda:")
    
    # Genera texto utilizando GPT-3
    prompt = "Mostrar las últimas tendencias de moda"
    response = generate_text(prompt, api_key)
    
    st.write(response)

# Función para la búsqueda de productos
def product_search(api_key):
    st.title("Búsqueda de productos")
    st.write("Aquí puedes buscar productos de moda:")
    
    # Genera texto utilizando GPT-3
    prompt = "Buscar productos de moda"
    response = generate_text(prompt, api_key)
    
    st.write(response)

# Función para las recomendaciones
def recommendations(api_key):
    st.title("Recomendaciones")
    st.write("Aquí puedes encontrar recomendaciones de moda:")
    
    # Genera texto utilizando GPT-3
    prompt = "Mostrar recomendaciones de moda"
    response = generate_text(prompt, api_key)
    
    st.write(response)

# Función principal para ejecutar la aplicación de Streamlit
def main():
    api_key = st.sidebar.text_input("Clave de API de OpenAI")
    
    page = st.sidebar.selectbox("Secciones", ["Inicio", "Últimas tendencias", "Búsqueda de productos", "Recomendaciones"])
    
    if page == "Inicio":
        home()
    elif page == "Últimas tendencias":
        latest_trends(api_key)
    elif page == "Búsqueda de productos":
        product_search(api_key)
    elif page == "Recomendaciones":
        recommendations(api_key)

if __name__ == "__main__":
    main()
