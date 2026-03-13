import streamlit as st

# Configuración de la página (Diseño minimalista)
st.set_page_config(
    page_title="Dashboard Educativo: IA en Salud Mental",
    page_icon="🧠",
    layout="centered"
)

# Estilo personalizado (CSS) para bordes redondeados y diseño limpio
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        height: 3em;
        background-color: #4A90E2;
        color: white;
        border: none;
    }
    .stExpander {
        border-radius: 15px;
        background-color: white;
        border: 1px solid #e1e4e8;
        margin-bottom: 10px;
    }
    .ref-card {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #4A90E2;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# 1. SECCIÓN DEL TÍTULO [cite: 3, 4, 6]
st.markdown("<h1 style='text-align: center; color: #2c3e50;'>El terapeuta en tu bolsillo: ¿Puede un algoritmo sanar la mente?</h1>", unsafe_allow_html=True)

# 2. SECCIÓN DEL RESUMEN [cite: 7, 8, 9]
st.markdown("### Resumen")
st.info("""
Imagina que a las tres de la mañana, ante una crisis de ansiedad, puedes hablar con una IA 
entrenada en ciencia psicológica. Este artículo explora si la Inteligencia Artificial es 
un simple plan B o la evolución definitiva de la terapia moderna. [cite: 42, 43, 45]
""")

st.divider()

# 3. SECCIÓN DE SUBTÍTULOS E INTERACTIVIDAD (Estructura de tarjetas/juego) [cite: 11, 12, 13, 15]
st.subheader("Explora las secciones del artículo")

# Tarjeta 1: Evolución
with st.expander("🔵 De las videollamadas al algoritmo inteligente"):
    st.write("""
    La telemedicina ha pasado de simples videollamadas a sistemas que aprenden del usuario[cite: 47, 49]. 
    Investigaciones indican que el formato digital es una alternativa real y efectiva, logrando resultados 
    idénticos a la terapia presencial[cite: 51]. Incluso, en casos de depresión, la terapia electrónica 
    ha mostrado ser ligeramente más efectiva[cite: 52].
    """)

# Tarjeta 2: Metodología
with st.expander("🟢 El código detrás de la empatía"):
    st.write("""
    La IA utiliza la Teoría Cognitivo-Conductual (TCC) por su estructura lógica basada en tareas[cite: 54, 55]. 
    Aunque los pacientes ya aceptan la terapia digital con rigor[cite: 58], el gran reto es la personalización: 
    la IA debe adaptarse a la complejidad de cada caso y no ser una "talla única"[cite: 59, 60].
    """)

# Tarjeta 3: Desafíos
with st.expander("🟡 El gran desafío: ¿Por qué abandonamos el tratamiento?"):
    st.write("""
    La adherencia es el mayor obstáculo: es más fácil ignorar una app que a un terapeuta humano[cite: 62, 63]. 
    La tasa de permanencia baja del 82.4% (presencial) al 72.9% (digital)[cite: 64]. La solución propuesta 
    es un modelo híbrido: tecnología con respaldo de un profesional humano[cite: 66, 67].
    """)

# Tarjeta 4: Futuro
with st.expander("🟣 El futuro: ¿Un mundo sin listas de espera?"):
    st.write("""
    El objetivo es democratizar el acceso a la salud mental, eliminando barreras geográficas y económicas[cite: 69, 70]. 
    No se busca reemplazar al psicólogo, sino potenciar su alcance uniendo el rigor científico con la 
    velocidad tecnológica[cite: 70, 71].
    """)

st.divider()

# 4. BOTÓN PARA MOSTRAR REFERENCIAS [cite: 21, 38]
if "show_refs" not in st.session_state:
    st.session_state.show_refs = False

def toggle_refs():
    st.session_state.show_refs = not st.session_state.show_refs

st.button("📚 Ver Referencias", on_click=toggle_refs)

# Visualización de referencias separadas [cite: 22, 23, 24, 25]
if st.session_state.show_refs:
    st.markdown("### Referencias Bibliográficas")
    
    # Referencia 1
    st.markdown("""
    <div class="ref-card">
    <strong>Hernández Pérez, D. S. (2026). IA y ética en la evaluación psicológica.</strong><br>
    <em>Resumen:</em> Analiza el uso de IA para reconocer patrones y facilitar diagnósticos, advirtiendo sobre 
    sesgos algorítmicos y la necesidad de mantener el juicio clínico humano. [cite: 75, 76, 78, 80]
    </div>
    """, unsafe_allow_html=True)
    
    # Referencia 2
    st.markdown("""
    <div class="ref-card">
    <strong>Infocop. (2025). El uso ético de la IA en la psicología: directrices de la APA.</strong><br>
    <em>Resumen:</em> Presenta recomendaciones de la APA sobre protección de datos y supervisión humana, 
    subrayando que la IA complementa pero no reemplaza la responsabilidad del profesional. [cite: 82, 83, 85, 87]
    </div>
    """, unsafe_allow_html=True)
    
    # Referencia 3
    st.markdown("""
    <div class="ref-card">
    <strong>PAR, Inc. (2025). The ethical use of AI in psychology.</strong><br>
    <em>Resumen:</em> Describe cómo la IA ahorra tiempo en tareas administrativas y reportes, permitiendo 
    que el psicólogo se enfoque más en la atención directa del paciente. [cite: 88, 90, 92]
    </div>
    """, unsafe_allow_html=True)

# Pie de página educativo
st.markdown("---")
st.caption("Dashboard Interactivo - Ciencia y Psicología 2026")
